import argparse
import os

import numpy as np
from PIL import Image
from polyaxon import tracking


def main(show_expected: bool):
    if show_expected:
        # expected behavior but non-standard approach
        print('show expected behavior')
        run = tracking.Run()
        outdir = f'/plx-artifacts/{run.run_uuid}/outputs/test_output'
    else:
        # standard approach with missing output
        print('show buggy behavior')
        run = tracking.Run()
        outputs_path = run.get_outputs_path()
        # variant which has the same buggy behavior
        # tracking.init()
        # outputs_path = tracking.get_outputs_path()
        outdir = os.path.join(outputs_path, 'test_output')

    os.makedirs(outdir)
    for idx in range(200):
        img_np = np.random.rand(32, 32, 3)
        img_rescaled = (255.0 / img_np.max() * (img_np - img_np.min())).astype(np.uint8)
        img_pil = Image.fromarray(img_rescaled)
        fpath = os.path.join(outdir, f'{idx}.png')
        img_pil.save(fpath)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--show_expected',
        type=bool,
        default=False)
    args = parser.parse_args()
    main(args.show_expected)