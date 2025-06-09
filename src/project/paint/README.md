# Paint Inverse Crop Helper

---

## Start the program

```bash
python paint_crop.py
```

---

### Example

Imagine the original image is:

```
1
2
3
4
5
```

If you select **3** and apply *inverse crop*, you will get:

```
1
2
4
5
```

---

## Features

---

### Skip animation

You can pass `n` to skip the startup animation:

```bash
python paint_crop.py n
```

---

### Debug information when you perform inverse crop

Example output:

```
=== inverse_crop version 1.1 ===
Selection (canvas coords): (630, 468) to (-10, 339)
Selection (clamped image coords): (0, 339) to (630, 468)
Image size: 640 x 701
Performing vertical cut (cutting out horizontal band)
New image size: (640, 572)
```

---

### Can slice vertically or horizontally

Example:

Original:

```
1234
4567
890*
```

If you select around `2`, `5`, `9` and apply *inverse crop*, you will get:

```
134
467
80*
```

---

### Notes

- Slice is **full width or full height**, even if you select only 90% — this is by design (feature).
- The program has **tooltips** for toolbar buttons.

---

## Screenshots

_Add a screenshot here showing the app window, toolbar, and inverse crop in action._

Example:

```
![Inverse Crop Helper Screenshot](screenshot.png)
```

---

## License

MIT License or personal use — you may modify and share.

---

## Credits

Developed by [tgkprog](https://github.com/tgkprog).

---