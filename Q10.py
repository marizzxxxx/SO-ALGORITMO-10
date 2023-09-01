import random

def fifo(pages, num_frames):
    frame_set = []
    page_faults = 0

    for page in pages:
        if page not in frame_set:
            if len(frame_set) == num_frames:
                frame_set.pop(0)
            frame_set.append(page)
            page_faults += 1

    return page_faults

def lru(pages, num_frames):
    frame_set = []
    page_faults = 0

    for page in pages:
        if page not in frame_set:
            if len(frame_set) == num_frames:
                frame_set.pop(0)
            frame_set.append(page)
            page_faults += 1
        else:
            frame_set.remove(page)
            frame_set.append(page)

    return page_faults

reference_string = [random.randint(0, 9) for _ in range(100)]

for num_frames in range(1, 6):
    fifo_faults = fifo(reference_string, num_frames)
    lru_faults = lru(reference_string, num_frames)
    print(f'Quadros: {num_frames} | FIFO Falhas de Página: {fifo_faults} | LRU Falhas de Página: {lru_faults}')
