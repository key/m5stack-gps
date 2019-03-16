def calc_checksum(data):
    ck_a = 0
    ck_b = 0

    i = 0

    while i < len(data):
        ck_a = (ck_a + data[i]) & 0xff
        ck_b = (ck_b + ck_a) & 0xff
        i += 1

    return ck_a, ck_b
