cmake_minimum_required(VERSION 3.20)

if(NOT DEFINED PATCH_VERSION)
    set(PATCH_VERSION "1" )
endif()


set(PROJECT_VESRION 0.0.${PATCH_VERSION})

project(helloworld VERSION ${PROJECT_VESRION})

add_executable(helloworld_cli main.cpp)

set_target_properties(helloworld_cli PROPERTIES
    CXX_STANDARD 17
    CXX_STANDARD_REQUIRED ON
) 
target_compile_definitions(helloworld_cli PUBLIC -DPATCH_VERSION=${PATCH_VERSION})
if (MSVC)
    target_compile_options(helloworld_cli PRIVATE
        /W4 
    )
else ()
    target_compile_options(helloworld_cli PRIVATE
        -Wall -Wextra -pedantic -Werror
    )
endif()



install(TARGETS helloworld_cli RUNTIME DESTINATION bin)

set(CPACK_GENERATOR DEB)

set(CPACK_PACKAGE_VERSION_MAJOR "${PROJECT_VERSION_MAJOR}")
set(CPACK_PACKAGE_VERSION_MINOR "${PROJECT_VERSION_MINOR}")
set(CPACK_PACKAGE_VERSION_PATCH "${PROJECT_VERSION_PATCH}")

set(CPACK_PACKAGE_CONTACT example@example.com)

include(CPack)
