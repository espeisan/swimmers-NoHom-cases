import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


filename = "data-grad1-1-steps500.txt"
CSV_fmt = dict(
    #header=None,
    sep=",", 
    )

if __name__ == "__main__":

    df = pd.read_csv(filename, **CSV_fmt)

    Pe = 60.0
    TrID = 0.2
    
    cmap='Blues'
    
    f,(ax1,ax2,ax3) = plt.subplots(1,3,gridspec_kw={'width_ratios':[1,1,1]}) #,sharex=True,sharey=True)
    ax = [ax1,ax2,ax3]
    ax1.get_shared_y_axes().join(ax2,ax3)
    
    rewID = ["Displacement","FDifference","FAccumulated"]    
    
    for R in range(len(rewID)):
    
       dff = df.loc[(df['TrID'] == TrID) & (df['Pe'] == Pe) & (df['rewID'] == rewID[R])]
       dff = dff[['alpha','gamma','learned']]
       dff = dff.pivot(index='alpha',columns='gamma',values='learned')
       g = sns.heatmap(dff,annot=True,cbar=False,ax=ax[R],vmin=-1,vmax=1,cmap=cmap)
       g.set_ylabel('')
       g.set_xlabel('')
       if R != 0: g.set_yticks([])
       ax[R].set_title(rewID[R])
    

    plt.tight_layout()
    plt.savefig(f"LRPe{str(Pe)}Tr{str(TrID)}.png", dpi=150)
    #plt.show()

