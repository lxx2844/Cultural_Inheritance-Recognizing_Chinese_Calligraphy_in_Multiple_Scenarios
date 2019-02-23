import os

train_task_id = 'ICDAR2015T640'
initial_epoch = 0
epoch_num = 24
lr = 1e-4
decay = 5e-4
# clipvalue = 0.5  # default 0.5, 0 means no clip
patience = 5
load_weights = True
lambda_inside_score_loss = 4.0
lambda_side_vertex_code_loss = 1.0
lambda_side_vertex_coord_loss = 1.0

total_img = 60000
validation_split_ratio = 0.1
max_train_img_size = int(train_task_id[-3:])
max_predict_img_size = int(train_task_id[-3:])  # 2400
assert max_train_img_size in [256, 384, 512, 640, 736], \
    'max_train_img_size must in [256, 384, 512, 640, 736]'
if max_train_img_size == 256:
    batch_size = 8
elif max_train_img_size == 384:
    batch_size = 4
elif max_train_img_size == 512:
    batch_size = 2
else:
    batch_size = 8
steps_per_epoch = 50000 // batch_size
validation_steps = 10000 // batch_size

# data_dir = '/home/huguanghao2/Data/DF_zh/train_dataset_char/'
data_dir = '/home/huguanghao2/Data/DF_zh/train_dataset_char/'
#=====================================================================#

origin_image_dir_name = 'train_Image/'
origin_txt_dir_name = 'train_lable.csv'

origin_val_image_dir_name = 'verify_Image/'
origin_val_txt_dir_name = 'verify_lable.csv'

origin_test_image_dir_name = '../test_dataset_char/'
origin_test_txt_dir_name = 'verify_lable.csv'

#======================================================================#

train_image_dir_name = 'images_%s/' % train_task_id
train_label_dir_name = 'labels_%s/' % train_task_id

val_image_dir_name = 'images_%s/' % train_task_id
val_label_dir_name = 'labels_%s/' % train_task_id

test_image_dir_name = 'images_test_%s/' % train_task_id
test_label_dir_name = 'labels_test_%s/' % train_task_id

#======================================================================#

show_gt_image_dir_name = 'show_gt_images_%s/' % train_task_id
show_act_image_dir_name = 'show_act_images_%s/' % train_task_id

gen_origin_img = True
draw_gt_quad = True
draw_act_quad = True

val_fname = 'val_%s.txt' % train_task_id
train_fname = 'train_%s.txt' % train_task_id
# in paper it's 0.3, maybe to large to this problem
shrink_ratio = 0.2
# pixels between 0.2 and 0.6 are side pixels
shrink_side_ratio = 0.6
epsilon = 1e-4

num_channels = 3
feature_layers_range = range(5, 1, -1)
# feature_layers_range = range(3, 0, -1)
feature_layers_num = len(feature_layers_range)
# pixel_size = 4
pixel_size = 2 ** feature_layers_range[-1]
locked_layers = False

if not os.path.exists('model'):
    os.mkdir('model')
if not os.path.exists('saved_model'):
    os.mkdir('saved_model')

checkpoint_path = 'checkpoints/weights_%s.{epoch:03d}-{val_loss:.3f}.h5' \
                     % train_task_id

load_weight = 'checkpoints/weights_ICDAR2015T640.001-0.587.h5'

saved_model_weights_file_path = 'saved_models/east_model_weights_%s.h5'\
                                 % train_task_id

pixel_threshold = 0.7
side_vertex_pixel_threshold = 0.9
trunc_threshold = 0.1
predict_cut_text_line = False
predict_write2txt = True

gpu = 1