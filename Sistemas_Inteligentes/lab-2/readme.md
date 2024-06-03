# Ontología de Fútbol

**Autor**: Ronaldo Jiménez
**Web**: jimcostdev.com

## Descripción

Esta ontología de fútbol está diseñada para representar información sobre torneos, equipos y partidos de fútbol. Incluye clases, propiedades de objeto y propiedades de datos relevantes para modelar estos conceptos. La ontología está creada en formato OWL y puede ser utilizada para gestionar y consultar datos relacionados con el fútbol.

## Estructura de la Ontología

### Clases

- **Torneo**: Representa un torneo de fútbol.
- **Equipo**: Representa un equipo de fútbol.
- **Partido**: Representa un partido de fútbol.

### Propiedades de Objeto

- **participa_en**: Relaciona un equipo con el torneo en el que participa.
- **tiene_partido**: Relaciona un torneo con los partidos que contiene.
- **equipo_local**: Relaciona un partido con el equipo local.
- **equipo_visitante**: Relaciona un partido con el equipo visitante.

### Propiedades de Datos

- **nombre**: El nombre de un torneo, equipo o partido.
- **fecha**: La fecha y hora de un partido.
- **resultado**: El resultado de un partido.
- **ciudad**: La ciudad de un equipo.
- **fundacion**: El año de fundación de un equipo.
- **capacidad**: La capacidad del estadio de un equipo.

## Ejemplo de Individuos

- **Torneo1**: Representa un torneo, por ejemplo, la Premier League.
- **ManchesterUnited**: Representa al equipo Manchester United.
- **Chelsea**: Representa al equipo Chelsea.
- **Arsenal**: Representa al equipo Arsenal.
- **Liverpool**: Representa al equipo Liverpool.
- **Partido1**: Representa un partido entre Manchester United y Chelsea.
- **Partido2**: Representa un partido entre Arsenal y Liverpool.
- **Partido3**: Representa un partido entre Liverpool y Manchester United.

## Aserciones de Propiedades

### Propiedades de Objeto

- **ManchesterUnited participa_en PremierLeague**
- **Chelsea participa_en PremierLeague**
- **Arsenal participa_en PremierLeague**
- **Liverpool participa_en PremierLeague**
- **PremierLeague tiene_partido Partido1**
- **PremierLeague tiene_partido Partido2**
- **PremierLeague tiene_partido Partido3**
- **Partido1 equipo_local ManchesterUnited**
- **Partido1 equipo_visitante Chelsea**
- **Partido2 equipo_local Arsenal**
- **Partido2 equipo_visitante Liverpool**
- **Partido3 equipo_local Liverpool**
- **Partido3 equipo_visitante ManchesterUnited**

### Propiedades de Datos

- **PremierLeague nombre "Premier League"**
- **ManchesterUnited nombre "Manchester United"**
- **Chelsea nombre "Chelsea"**
- **Arsenal nombre "Arsenal"**
- **Liverpool nombre "Liverpool"**
- **Partido1 fecha "2024-05-20T15:00:00"**
- **Partido1 resultado "2-1"**
- **Partido2 fecha "2024-05-21T18:00:00"**
- **Partido2 resultado "0-0"**
- **Partido3 fecha "2024-05-22T20:00:00"**
- **Partido3 resultado "1-3"**
- **ManchesterUnited ciudad "Manchester"**
- **ManchesterUnited fundacion "1878"**
- **ManchesterUnited capacidad 74879**
- **Chelsea ciudad "Londres"**
- **Chelsea fundacion "1905"**
- **Chelsea capacidad 41837**
- **Arsenal ciudad "Londres"**
- **Arsenal fundacion "1886"**
- **Arsenal capacidad 60260**
- **Liverpool ciudad "Liverpool"**
- **Liverpool fundacion "1892"**
- **Liverpool capacidad 53394**


