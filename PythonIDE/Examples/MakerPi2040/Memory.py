import gc
import micropython

print('Memory Free:', "{:,}".format(gc.mem_free()), 'bytes')
print('Memory Allocated:', "{:,}".format(gc.mem_alloc()), 'bytes')
    