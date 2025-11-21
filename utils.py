import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
#%matplotlib inline
import matplotlib
matplotlib.rcParams["figure.figsize"]=(20,10)
import seaborn as sns;sns.set()
import warnings
warnings.filterwarnings('ignore')
import plotly.express as px
from datetime import datetime,time
from plotly.offline import iplot,plot,init_notebook_mode,download_plotlyjs
#%matplotlib inline 
init_notebook_mode(connected=True)


from scipy.stats import spearmanr,mannwhitneyu
def mannwhitneyu_func(Dataset:pd.DataFrame,Numericaltarget:str,BinaryFeature:str):
    group1 = Dataset[Numericaltarget][Dataset[BinaryFeature] == 0]
    group2 = Dataset[Numericaltarget][Dataset[BinaryFeature]  == 1]
    u_stat, p_mw = mannwhitneyu(group1, group2, alternative='two-sided')
    print(f"W = {u_stat:.3f}, p = {p_mw:.3f}")
    if p_mw < 0.05:
        print(f"As The P-value is less than .05 : Reject H₀ → There is significant distribution difference between {Numericaltarget} & {BinaryFeature} (typically medians)")
    else:
        print(f"As The P-value is more than .05 : Fail to reject H₀ → No significant distribution difference between {Numericaltarget} & {BinaryFeature} (typically medians)")

    stat, p = mannwhitneyu(group1, group2, alternative='greater')    
    if p < 0.05 :
        print(f"more over this suggest that the group 1 {BinaryFeature} ==0 () tend to have higher price values than group 2 {BinaryFeature} ==1")   
    else:
        print(f"more over this suggest that the group 2 {BinaryFeature} ==1 () tend to have higher price values than group 1 {BinaryFeature} ==0")     

    fig, axes = plt.subplots(1, 3, figsize=(20, 5))
    sns.boxplot(x=BinaryFeature, y=Numericaltarget, data=Dataset, palette="Set2",ax=axes[0])
    sns.stripplot(x=BinaryFeature, y=Numericaltarget, data=Dataset, color="black", alpha=0.6,ax=axes[1]);
    sns.histplot(x=Numericaltarget,hue=BinaryFeature,ax=axes[2],data=Dataset,alpha=0.6)



def spearmanr_func(Dataset:pd.DataFrame,Numericaltarget:str,OrdinalFeature:str):
    spearman_corr, p_spear = spearmanr(Dataset[Numericaltarget],Dataset[OrdinalFeature])
    prob_df = Dataset.groupby(OrdinalFeature)[Numericaltarget].mean().reset_index()
    prob_df.rename(columns={Numericaltarget: 'prob_target_1'}, inplace=True)  

    print(f"spearman_corr = {spearman_corr:.3f}, p = {p_spear:.3f}")
    if p_spear < 0.05:
        print(f"As The P-value is less than .05 : Reject H₀ → There is significant monotonic relationship between {Numericaltarget} & {OrdinalFeature}")
    else:
        print(f"As The P-value is more than .05 : Fail to reject H₀ → No significant monotonic relationship between {Numericaltarget} & {OrdinalFeature}")

    if spearman_corr > 0:
        print(f"more over this suggest that the As the {OrdinalFeature} variable increases, the {Numericaltarget} variable tends to increase (positive association).")
    else:
        print(f"more over this suggest that the As the {OrdinalFeature} variable increases, the {Numericaltarget} variable tends to decrease (negative association).")    
            

    plt.figure(figsize=(20,5))
    ax=sns.heatmap(prob_df.set_index(OrdinalFeature).T, annot=True, cmap="YlGnBu", cbar=True)
    ax.set_title("Probability of Binary Target=1 by Ordinal Feature")
    ax.set_xlabel("Ordinal Feature")
    ax.set_ylabel("Probability")
    plt.tight_layout()
    plt.show()      


import scikit_posthocs as sp
def posthoc_dunn_test(Dataset,Numericaltarget,CategoricalFeature):
    import scikit_posthocs as sp
    posthoc = sp.posthoc_dunn(Dataset, val_col=Numericaltarget, group_col=CategoricalFeature, p_adjust='bonferroni')
    plt.figure(figsize=(20,7))
    ax=sns.heatmap(posthoc.round(2),annot=True,cmap="Reds")
    ax.set_title(f"posthoc_dunn test -p_adjust- between {Numericaltarget} and {CategoricalFeature} groups")
    print("if p_adjust < .05 ==> significant difference between those two groups.")


def kruskal_func(Dataset:pd.DataFrame,Numericaltarget:str,CategoricalFeature:str):
    from scipy.stats import kruskal
    groups = [Dataset[Dataset[CategoricalFeature] == level][Numericaltarget] for level in Dataset[CategoricalFeature].unique()]

    stat, p = kruskal(*groups)
    if p < 0.05: 
        print(f"Kruskal-Wallis Test: Statistic={stat:.3f}, P-value={p:.3f} ==>\n The p value less than 0.05 ==> At least one group has Significant difference")
    else:
        print(f"Kruskal-Wallis Test: Statistic={stat:.3f}, P-value={p:.3f} ==>\n the p value more than 0.05 ==> No Significant difference between groups")

    fig, axes = plt.subplots(1, 2, figsize=(20, 5))
    sns.boxplot(x=CategoricalFeature, y=Numericaltarget, data=Dataset, palette="Set2",ax=axes[0])
    sns.stripplot(x=CategoricalFeature, y=Numericaltarget, data=Dataset, color="black", alpha=0.6, jitter=True,ax=axes[1])
    plt.title(f"Kruskal–Wallis Test\nH={stat:.2f}, p={p:.4f}")
    plt.show()

    if p < 0.05:
        print("As At least one group has Significant difference --> posthoc_dunn test")
        posthoc_dunn_test(Dataset,Numericaltarget,CategoricalFeature)    
