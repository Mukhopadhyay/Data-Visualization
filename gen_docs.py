import os

images = os.listdir('gallery/Histogram')

strings = []

for i in range(0, len(images), 2):
    try:
        im1, im2 = images[i], images[i+1]
        # strings.append(f'|_{im1}_|_{im2}_|')
        # strings.append( '|:------|:------|')
        string = f'<img src="gallery/Histogram/{im1}" width="40%"> <img src="gallery/Histogram/{im2}" width="40%">'
    except IndexError:
        im1 = images[i]
        string = f'<img src="gallery/Histogram/{im1}">'
    finally:
        strings.append(string+'\n')

with open('test.md', 'w') as file:
    file.write('\n'.join(strings))

print('created test.md!')
