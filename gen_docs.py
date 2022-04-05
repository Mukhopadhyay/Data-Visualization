import os

directories = [
    ('Histogram', {
        'mpl': 'Matplotlib',
        'sns': 'Seaborn',
        'gg': 'Plotnine',
        'px': 'Plotly'
    })
]

for dir, mapping in directories:
    images = os.listdir(f'gallery/{dir}')

    strings = [f'# {dir}',]

    # Breaking down the images into subsections
    for ext, name in mapping.items():
        ims = [x for x in images if x.startswith(ext)]
        strings.append(f'## {name}')

        for i in range(0, len(ims), 2):
            try:
                im1, im2 = ims[i], ims[i+1]
                # strings.append(f'|_{im1}_|_{im2}_|')
                # strings.append( '|:------|:------|')
                string = f'<img src="../gallery/Histogram/{im1}" width="45%"> <img src="../gallery/Histogram/{im2}" width="45%">'
            except IndexError:
                im1 = ims[i]
                string = f'<img src="../gallery/Histogram/{im1}" width="45%">'
            finally:
                strings.append(string+'\n')


    # for i in range(0, len(images), 2):
    #     try:
    #         im1, im2 = images[i], images[i+1]
    #         # strings.append(f'|_{im1}_|_{im2}_|')
    #         # strings.append( '|:------|:------|')
    #         string = f'<img src="gallery/Histogram/{im1}" width="40%"> <img src="gallery/Histogram/{im2}" width="40%">'
    #     except IndexError:
    #         im1 = images[i]
    #         string = f'<img src="gallery/Histogram/{im1}">'
    #     finally:
    #         strings.append(string+'\n')

    fname = os.path.join(dir, 'README.md')
    with open(fname, 'w') as file:
        file.write('\n'.join(strings))

    print(f'Saved @ {fname}')
