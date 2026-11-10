# Encerrados, pero no solos — Escape Room Educativo

Proyecto de práctica pedagógica (Tecnología e Informática, grado 8°): un escape room presencial para que el curso deje de fragmentarse en grupitos y aprenda, jugando, a trabajar en equipo.

## Archivos

| Archivo | Qué es |
| --- | --- |
| `escape-room-presentacion.html` | La presentación completa. Ábrela en el navegador; desde ahí se entra a la Arena. Funciona sin internet (los videos y la Arena van dentro del archivo). |
| `arena-contrarreloj.html` | La Arena Contrarreloj por separado: equipos, vidas, cronómetro, historia y dado de retos. Se puede abrir sola. |
| `docs/Arena_Contrarreloj_Manual_12_Retos.docx` | Manual de los 12 retos (materiales, preparación, soluciones). |
| `tools/embed_arena.py` | Vuelve a meter la Arena dentro de la presentación después de editarla. |

## Cómo se juega una partida

1. **Registrar el equipo** (4 jugadores) y pulsar **▶ Iniciar** cuando empiece a correr el tiempo.
2. **Leer la historia** «Nadie escapa solo» en el panel 📖:
   - **Siguiente ▶** (o la flecha →) muestra el siguiente párrafo para que lo lea quien facilita.
   - **🔊 Leer en voz alta** narra la historia sola con la voz del navegador (elige automáticamente una voz en español).
3. **Momentos de reto**: al llegar a uno de los huecos de la narrativa aparece el **dado** y sortea un reto según la dificultad:

   | Momento | Dificultad (orden progresivo) |
   | --- | --- |
   | 1 · después de «Nudo» | Fácil (retos 1–4) |
   | 2 · después de «Desenlace inicial» | Medio (retos 5–8) |
   | 3 · después de «El giro» | Difícil (retos 9–11) |
   | 4 · después de «El verdadero obstáculo» | Libre: el dado elige primero la dificultad y luego el reto |
   | 5 · la caja fuerte | Siempre el reto 12, «La caja fuerte: nadie escapa solo» |

   - Un mismo equipo nunca repite reto.
   - **↻ Otro reto** descarta el que salió (por ejemplo, si no hay materiales) y lanza de nuevo.
   - **Saltar** sigue la historia sin hacer ese reto (útil si el tiempo no alcanza).
   - En **orden caótico** el dado decide también la dificultad de cada reto. El orden se elige antes del primer reto.
4. **Ficha del reto**: muestra la introducción para leer en voz alta, las instrucciones y, plegados, los materiales, la pista y la solución (para que no se vean en el proyector). Al terminar se marca **✔ ¡Lo lograron!** o **✖ No lo lograron** y aparece el cierre narrativo.
5. **Caja fuerte**: al marcar **🔓 ¡Abrieron la caja fuerte!** se detiene el reloj y se registra la victoria; la historia sigue con el mensaje final y la reflexión. Al final, **🏆 Ver resultado** muestra el puntaje.

La tabla de posiciones guarda, para cada equipo, qué retos le salieron y si los superó.

## Cambiar la configuración

En `arena-contrarreloj.html`:

- `CONFIG` (al inicio del código): número de equipos, vidas, duración (`DURATION`, hoy 10 minutos) y puntos.
- `HUECOS`: qué dificultad usa cada momento de reto. Por ejemplo, `{ fijo: 12 }` hace que el último momento sea siempre la caja fuerte; cambiarlo por `{ nivel: 'dificil' }` lo sortea con el dado.
- `RETOS`: el texto de los 12 retos, tomado del manual.

Después de editar la Arena, actualiza la presentación:

```bash
python3 tools/embed_arena.py
```
