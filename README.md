# SCHP python package

[SCHP](https://github.com/GoGoDuck912/Self-Correction-Human-Parsing.git) is clothes segmentation model.

This repository wrapped SCHP to python package. </br>


## Installing
```bash
pip install schp
```

## Usage
```python
    image_path = 'IMAGE.png'
    dataset_type = "lip" ### lip, atr, pascal
    model_dir = 'CHECKPOINT_DIR'

    images = [
        cv2.imread(image_path, cv2.IMREAD_COLOR),
        cv2.imread(image_path, cv2.IMREAD_COLOR),
    ]
    images = np.stack(images)

    schp_model = schp.SCHP(dataset_type, model_dir)
    
    human_parsing_results = schp_model.parse(
        images=images, 
    )
    print(human_parsing_results.shape)

    label = schp_model.get_label()
    print(label)

```
