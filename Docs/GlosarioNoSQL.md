Aquí hay un glosario de términos estándar utilizados en bases de datos NoSQL como Redis, MongoDB, RethinkDB y otras:

- Documento: La estructura/unidad de datos básica se almacena en MongoDB y CouchDB. Un documento es análogo a una fila en una tabla de base de datos relacional. Los documentos se almacenan en formato similar a JSON.

- Colección: un grupo de documentos de MongoDB. Similar a una tabla en una base de datos relacional.

- Valor-clave: la estructura/unidad de datos básica almacenada en Redis y UnQLite. Los datos se almacenan como un par campo-valor, siendo el campo la clave.

- Espacio de claves: el conjunto de todas las claves posibles que se pueden almacenar en una base de datos NoSQL como Redis.

- Valor: en los almacenes clave-valor, el valor asociado a una clave. Puede ser una cadena, una lista, un hash, etc. según el tipo de datos.

- Tipo de datos: el tipo de un valor almacenado. Los tipos comunes incluyen cadena, lista, conjunto, conjunto ordenado y hash.

- Indexación: creación de un índice en uno o más campos de documentos en MongoDB para admitir búsquedas y consultas más rápidas.

- Fragmentación: partición horizontal de datos en varias máquinas en una implementación de MongoDB para una mayor escalabilidad de escritura/lectura.

- Replicación: mantener copias de datos en varias máquinas para lograr redundancia y alta disponibilidad.

- Modelos de coherencia: cómo se propagan las actualizaciones entre réplicas: eventuales, fuertes, casuales, etc.

- Teorema de CAP: Ningún sistema puede proporcionar simultáneamente coherencia, disponibilidad y tolerancia de partición.

- CRUD: Crear, Leer, Actualizar, Eliminar: las operaciones de datos básicas admitidas.

- Cursor: la interfaz del iterador para consultar e iterar resultados en MongoDB.

- Flujo de cambios: vista en tiempo real de los cambios de datos para aplicaciones reactivas en MongoDB.

- Stream: secuencia ordenada de eventos de datos en tiempo real en bases de datos KV como Redis. Usado para pub/sub.

- Pub/sub: modelo de mensajería de publicación/suscripción donde los clientes publican mensajes en canales/temas y otros se suscriben para recibir notificaciones.

- Durabilidad: la capacidad de la base de datos para sobrevivir fallas sin pérdida de datos, a través de mecanismos como fsync, AOF, registro en diario, etc.

- JSON/BSON: formatos de serialización de datos utilizados por MongoDB y otros. BSON agrega tipos.
