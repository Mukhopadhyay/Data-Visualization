import os
import matplotlib.pyplot as plt


def save_mpl(imname: str, base: str='../gallery', **kwargs) -> None:
    fname: str = os.path.join(base, imname)
    plt.savefig(fname, **kwargs)


save_sns = save_mpl


def save_px(fig, imname: str, base: str='../gallery', **kwargs) -> None:
    fname: str = os.path.join(base, imname)
    fig.write_image(fname, **kwargs)


def save_gg(fig, imname: str, base: str='../gallery', **kwargs) -> None:
    fname: str = os.path.join(base, imname)
    fig.save(fname, **kwargs)
