CC=gcc
CROSS_COMPILE=x86_64-w64-mingw32-
CFLAGS=-std=c99 -Wall -Wextra

all: secureFlagChecker.exe

.PHONY: clean
clean:
	rm inner.dll inner.dll.encrypted inner_binary.h secureFlagChecker.exe

inner.dll: inner.c
	$(CROSS_COMPILE)$(CC) $(CFLAGS) -shared -o $@ $^ $(LDFLAGS)

inner.dll.encrypted: inner.dll
	python process_xor.py $^ $@ 1234fade

inner_binary.h: inner.dll.encrypted
	xxd -i $^ > $@

secureFlagChecker.exe: outer.c inner_binary.h
	$(CROSS_COMPILE)$(CC) $(CFLAGS) -o $@ $^ $(LDFLAGS)