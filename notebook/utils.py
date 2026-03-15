def name_fix (query, df):
    query['library_name'] = query['library_name'].replace({
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

    df['LFPL_NAME'] = df['LFPL_NAME'].replace({
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

def lfpl_map (zipcodes, df, item, title, pe, plt):
    ax = zipcodes.plot(
        figsize=(10, 10),
        color='grey',
        edgecolor='grey',
        alpha=0.5
    )

    df.plot(
        ax=ax,
        column=item,
        cmap='Oranges',
        legend=True,
        markersize=df[item] / df[item].max() * 300
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

    plt.show()

