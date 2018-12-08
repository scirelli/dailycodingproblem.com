LDFLAGS=-std=c11 -g
objects=main.o XORLinkList.o

all: xorll

xorll: $(objects)
	gcc ${LDFLAGS} -o xorll $(objects)

main.o: XORLinkList.h
	gcc ${LDFLAGS} -c main.c
XORLinkList.o: XORLinkList.h
	gcc ${LDFLAGS} -c XORLinkList.c

.PHONY: clean
clean:
	rm -f xorll *.o

.PHONY: debug
debug:
	gdb xorll

run:
	./xorll; echo $$?;
