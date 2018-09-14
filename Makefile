CXX = $(shell root-config --cxx)
LD = $(shell root-config --ld)

INC=$(shell pwd)


STDINCDIR :=-I$(INC)/include
STDLIBDIR :=

CPPFLAGS := $(shell root-config --cflags) $(STDINCDIR)
LDFLAGS := $(shell root-config --glibs) $(STDLIBDIR) -lRooFit -lRooFitCore

CPPFLAGS += -g -std=c++1y

TARGET  = FitMgg

SRC  = scripts/read_histo.cc

OBJ = $(SRC:.cc=.o)

all : $(TARGET)

$(TARGET) : $(OBJ)
	$(LD) $(CPPFLAGS) -o $(TARGET) $(OBJ) $(LDFLAGS)
	@echo $
	@echo $<
	@echo $^


%.o : %.cc
	$(CXX) $(CPPFLAGS) -o $@ -c $<
	@echo $@
	@echo $<
clean :
	rm -f *.o app/*.o test/*.o src/*.o scripts/*.o $(TARGET) *~
