from collections import namedtuple


HParams = namedtuple('HParams', ['num_mels', 'rescale', 'rescaling_max', 'n_fft',
                                 'hop_size', 'win_size', 'sample_rate', 'frame_shift_ms',
                                 'signal_normalization', 'allow_clipping_in_normalization',
                                 'symmetric_mels', 'max_abs_value', 'preemphasize', 'preemphasis',
                                 'min_level_db', 'ref_level_db', 'fmin', 'fmax'])

# Default hyperparameters
hparams = HParams(
    num_mels=80,
    rescale=True,
    rescaling_max=0.9,
    n_fft=800,
    hop_size=200,
    win_size=800,
    sample_rate=16000,
    frame_shift_ms=None,
    signal_normalization=True,
    allow_clipping_in_normalization=True,
    symmetric_mels=True,
    max_abs_value=4.,
    preemphasize=True,
    preemphasis=0.97,
    min_level_db=-100,
    ref_level_db=20,
    fmin=55,
    fmax=7600,
)
