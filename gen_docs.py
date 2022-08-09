import os

# Extension and their mapping
ext_mapping = {
    'mpl': 'Matplotlib',
    'sns': 'Seaborn',
    'gg': 'Plotnine (ggplot)',
    'px': 'Plotly'
}

# Keep the directory and used framework mapping here
# Later down the road, this would be moved to some other file
directories = [
    ('Histogram', ext_mapping),
    ('Piechart', ext_mapping),
    ('Heatmap', ext_mapping),
    ('Scatterplot', ext_mapping)
]


# Generate the markdowns based on above directories list
if __name__ == '__main__':
    for dir, mapping in directories:
        images = os.listdir(f'gallery/{dir}')

        strings = [f'# {dir}',]

        # Breaking down the images into subsections
        for ext, name in mapping.items():

            ims = [x for x in images if x.startswith(ext)]
            strings.append(f'## {name}\nPlots created using the package `{name}`\n')

            for i in range(0, len(ims), 2):
                try:
                    im1, im2 = ims[i], ims[i+1]
                    string = f'<img src="../gallery/{dir}/{im1}" width="45%" height="300px"> <img src="../gallery/{dir}/{im2}" width="45%" height="300px">'
                except IndexError:
                    im1 = ims[i]
                    string = f'<img src="../gallery/{dir}/{im1}" width="45%" height="300px">'
                finally:
                    strings.append(string+'\n')

        fname = os.path.join(dir, 'README.md')
        with open(fname, 'w') as file:
            file.write('\n'.join(strings))

        print(f'Saved @ {fname}')
