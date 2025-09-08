# Terminal/Shell Linux

Guía de referencia rápida con comandos básicos para el manejo de una terminal Linux.

## Comandos Básicos

| Comando/Sentencia | Concepto/Descripción |
|--|--|
| `clear` o `Ctrl + L` | Limpiar pantalla de la terminal |
| `pwd` | Mostrar el directorio actual (print working directory) |
| `ls` | Listar el contenido de un directorio |
| `ls --help` | Mostrar todas las opciones disponibles para el comando `ls` |
| `ls -l` | Mostrar listado detallado con permisos, propietario, tamaño y fecha. La primera letra indica el tipo: `d` = directorio, `l` = enlace, `-` = archivo. Los siguientes caracteres (`r`, `w`, `x`) indican permisos de lectura, escritura y ejecución |
| `ls -lh` | Mostrar listado detallado con tamaños en formato legible (KB, MB, GB) |
| `alias` | Ver listado de alias creados en la sesión actual |
| `alias ls='ls -lh --color=auto'` | Crear un alias personalizado (actúa como una variable o atajo) |

## Navegación de Directorios

| Comando | Descripción |
|--|--|
| `cd` | Cambiar de directorio (change directory) |
| `cd .` | Permanecer en el directorio actual |
| `cd ..` | Retroceder un nivel en la jerarquía de directorios |
| `cd -` | Volver al directorio anterior (último directorio visitado) |
| `cd ~` | Ir al directorio home del usuario actual |

## Visualización de Archivos

| Comando | Descripción |
|--|--|
| `cat archivo.txt` | Mostrar todo el contenido de un archivo |
| `cat -n archivo.txt` | Mostrar contenido con numeración de líneas |

## Gestión de Archivos y Directorios

| Comando | Descripción |
|--|--|
| `touch archivo.ext` | Crear un archivo vacío |
| `echo "texto" > archivo.txt` | Crear archivo con contenido específico (sobrescribe si existe) |
| `echo "texto" >> archivo.txt` | Agregar contenido al final de un archivo existente |
| `mkdir directorio` | Crear un directorio |
| `mkdir -p ruta/completa/anidada` | Crear estructura de directorios anidados |
| `cp origen destino` | Copiar archivos |
| `cp -r directorio_origen directorio_destino` | Copiar directorios de forma recursiva |
| `mv origen destino` | Mover o renombrar archivos y directorios |
| `rm archivo.ext` | Eliminar archivos |
| `rm -i archivo.ext` | Eliminar archivo con confirmación interactiva |
| `rm -rf directorio` | Eliminar directorio y contenido de forma recursiva y forzada |

## Búsqueda de Archivos

| Comando | Descripción |
|--|--|
| `find . -name "*.ext"` | Buscar archivos por extensión en directorio actual |
| `find . -iname "archivo.txt"` | Buscar sin distinguir mayúsculas/minúsculas |
| `find . -type d -name "directorio"` | Buscar solo directorios con nombre específico |

## Administración del Sistema

| Comando | Descripción |
|--|--|
| `sudo comando` | Ejecutar comando con privilegios de superusuario |
| `sudo apt install paquete` | Instalar software usando el gestor de paquetes APT (Ubuntu/Debian) |

---

## Editor VIM

Vim es un editor de texto potente disponible en la mayoría de sistemas Unix/Linux.

### Comandos Básicos de VIM

| Comando | Descripción |
|--|--|
| `i` | Entrar en modo inserción (INSERT) |
| `:w` | Guardar archivo |
| `:q` | Salir de Vim (solo si no hay cambios sin guardar) |
| `:q!` | Salir forzadamente descartando cambios |
| `:wq` | Guardar y salir |

### Navegación en VIM

| Comando | Descripción |
|--|--|
| `gg` | Ir al inicio del documento |
| `GG` | Ir al final del documento |
| `0` | Ir al inicio de la línea actual |
| `$` | Ir al final de la línea actual |

### Edición en VIM

| Comando | Descripción |
|--|--|
| `u` | Deshacer último cambio |
| `Ctrl + r` | Rehacer cambio deshecho |
| `dd` | Cortar línea completa |
| `yy` | Copiar línea completa |
| `p` | Pegar contenido cortado o copiado |
| `x` | Eliminar carácter a la derecha del cursor |
| `X` | Eliminar carácter a la izquierda del cursor |
| `v` | Entrar en modo visual para seleccionar texto |

### Búsqueda y Reemplazo en VIM

| Comando | Descripción |
|--|--|
| `/texto` | Buscar texto en el documento |
| `n` | Ir a la siguiente coincidencia |
| `N` | Ir a la coincidencia anterior |
| `:%s/texto/nuevo_texto/g` | Reemplazar todas las ocurrencias en el documento |

---

## Tips Adicionales

- Utiliza `Tab` para autocompletado de nombres de archivos y comandos
- `Ctrl + C` para cancelar un comando en ejecución
- `history` para ver comandos ejecutados anteriormente
- `man comando` para acceder al manual de cualquier comando
