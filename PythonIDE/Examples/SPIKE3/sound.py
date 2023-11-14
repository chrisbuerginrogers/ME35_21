from hub import sound

sound.beep(220)
sound.beep(440,         # frequency
    500,                # duration msec
    100,                # volume 0 - 100
    attack = 0,         # msec increase to full volume
    decay = 0,          # msec decrease to sustain level 
    sustain = 100,      # msec length of note (until key release
    release = 0,        # msec time to decay to zero
    transition = 10,    # msec time to replace any note currently plauing
    waveform = sound.WAVEFORM_SINE, 
    channel = sound.DEFAULT)  # also sound.ANY - but not sure why this is here as there is only one speaker

sound.stop()

sound.volume(80) # (0-100)
