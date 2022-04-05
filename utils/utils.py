import os
from typing import Optional
import matplotlib.pyplot as plt


# Saves the current matplotlib figure
def save_mpl(idx: int, imname: Optional[str]='mpl', base: str='../gallery', **kwargs) -> None:
    dirname = os.path.split(os.path.abspath('.'))[1]
    imname = f'{imname}-{dirname}-{idx}.png'
    base = os.path.join(base, dirname)
    fname: str = os.path.join(base, imname)
    plt.savefig(fname, **kwargs)


# Saves the current seaborn figure
def save_sns(idx: int, imname: Optional[str]='sns', base: str='../gallery', **kwargs) -> None:
    dirname = os.path.split(os.path.abspath('.'))[1]
    imname = f'{imname}-{dirname}-{idx}.png'
    base = os.path.join(base, dirname)
    fname: str = os.path.join(base, imname)
    plt.savefig(fname, **kwargs)


# Saves the given plotly plot
def save_px(fig, idx: int, imname: Optional[str]='px', base: str='../gallery', **kwargs) -> None:
    dirname = os.path.split(os.path.abspath('.'))[1]
    imname = f'{imname}-{dirname}-{idx}.png'
    base = os.path.join(base, dirname)
    fname: str = os.path.join(base, imname)
    fig.write_image(fname, **kwargs)


# Saves the given ggplot object
def save_gg(fig, idx: int, imname: Optional[str]='gg', base: str='../gallery', **kwargs) -> None:
    dirname = os.path.split(os.path.abspath('.'))[1]
    imname = f'{imname}-{dirname}-{idx}.png'
    base = os.path.join(base, dirname)
    fname: str = os.path.join(base, imname)
    fig.save(fname, **kwargs)
