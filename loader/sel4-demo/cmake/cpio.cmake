# SPDX-License-Identifier: BSD-2-Clause
# Portable archive generation for the macOS host; original seL4 loader unchanged.
function(MakeCPIO output_name input_files)
  cmake_parse_arguments(MAKE_CPIO "" "CPIO_SYMBOL" "DEPENDS" ${ARGN})
  separate_arguments(asm_flags NATIVE_COMMAND "${BASE_ASM_FLAGS}")
  add_custom_command(OUTPUT ${output_name}
    COMMAND python3 "${CMAKE_SOURCE_DIR}/make_cpio.py" "${CMAKE_CURRENT_BINARY_DIR}/archive.cpio" ${input_files}
    COMMAND ${CMAKE_C_COMPILER} ${asm_flags} -c archive.S -o ${output_name}
    DEPENDS ${input_files} "${CMAKE_SOURCE_DIR}/make_cpio.py" ${MAKE_CPIO_DEPENDS}
    VERBATIM)
endfunction()
