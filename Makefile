all: builder
	sudo docker run --rm -it -v $(shell pwd):/code -w /code opencv-wasm make build

builder:
	sudo docker build -t opencv-wasm .

build: clean
	mkdir build
	cd build && emcmake cmake ..
	cd build && emmake make

clean:
	rm -rf build

serve:
	python3 serve.py
