This repo replicates the error in [pyvista #256](https://github.com/pyvista/pyvista/issues/256)

To run the project (this is just an example, you need to modify it properly):

```sh
export SRC_DIR=${pwd}
export BUILD_DIR=$SRC_DIR/build/
export my_libraries_path=/home/sik/miniconda3/envs/pyvista_cxx/lib/cmake/

mkdir -p $BUILD_DIR && cd $BUILD_DIR
rm $BUILD_DIR/* -Rf
cmake $SRC_DIR -DCMAKE_LIBRARY_PATH=$my_libraries_path
               -DCMAKE_CXX_STANDARD=11 \
               -DCMAKE_BUILD_TYPE=Debug \
               -DCMAKE_C_FLAGS_DEBUG="-g -O0" \
               -DCMAKE_CXX_FLAGS_DEBUG="-g -O0" \

make VERBOSE=1
```
