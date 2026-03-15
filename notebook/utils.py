def name_fix (df1, name1, df2, name2):
    df1[name1] = df1[name1].replace({
        'BON AIR': 'Bon Air',
        'FAIRDALE': 'Fairdale',
        'IROQUOIS': 'Iroquois',
        'CRESCENT HILL': 'Crescent Hill',
        'JEFFERSONTOWN': 'Jeffersontown',
        'HIGHLANDS-SHELBY PARK': 'Highlands',
        'MIDDLETOWN': 'Middletown',
        'PORTLAND': 'Portland',
        'SHIVELY': 'Shively',
        'PARKLAND': 'Parkland',
        'SHAWNEE': 'Shawnee',
        'MAIN': 'Main',
        'WESTERN': 'Western',
        'NEWBURG': 'Newburg',
        'FERN CREEK': 'Fern Creek',
        'ST. MATTHEWS': 'St. Matthews',
        'SOUTH CENTRAL REGIONAL': 'South Central',
        'NORTHEAST REGIONAL': 'Northeast',
        'SOUTHWEST REGIONAL': 'Southwest'
    })

    df2[name2] = df2[name2].replace({
        'BON AIR': 'Bon Air',
        'FAIRDALE': 'Fairdale',
        'IROQUOIS': 'Iroquois',
        'CRESCENT HILL': 'Crescent Hill',
        'JEFFERSONTOWN': 'Jeffersontown',
        'HIGHLANDS-SHELBY PARK': 'Highlands',
        'MIDDLETOWN': 'Middletown',
        'PORTLAND': 'Portland',
        'SHIVELY': 'Shively',
        'PARKLAND': 'Parkland',
        'SHAWNEE': 'Shawnee',
        'MAIN': 'Main',
        'WESTERN': 'Western',
        'NEWBURG': 'Newburg',
        'FERN CREEK': 'Fern Creek',
        'ST. MATTHEWS': 'St. Matthews',
        'SOUTH CENTRAL REGIONAL': 'South Central',
        'NORTHEAST REGIONAL': 'Northeast',
        'SOUTHWEST REGIONAL': 'Southwest'
    })

def lfpl_map (zipcodes, df, item, title, pe, plt, png_save):
    ax = zipcodes.plot(
        figsize=(10, 10),
        color='grey',
        edgecolor='grey',
        alpha=0.7
    )

    size = ((df[item] - df[item].min()) / (df[item].max() - df[item].min())) * 800 + 50
    df.plot(
        ax=ax,
        column=item,
        cmap='Oranges',
        legend=True,
        markersize=size
    )

    ax.set_title(title, fontsize=12)
    ax.axis("off")

    for x, y, name in zip(
        df.geometry.x,
        df.geometry.y,
        df["LFPL_NAME"]
    ):
    
        ax.text(
            x + 0.002,  # horizontal offset
            y + 0.002,  # vertical offset
            name,
            fontsize=7,
            color="black",
            ha="center",
            va="bottom",
            path_effects=[
            pe.withStroke (linewidth=2, foreground='white')   
            ]
        )

    plt.savefig(png_save)
    plt.show()
    

