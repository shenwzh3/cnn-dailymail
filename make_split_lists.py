import os,sys
import json
import glob

home_path = '/home/zhanwj/Desktop/yyy'
data_path = 'data/bytecup'
data_path = os.path.join(home_path, data_path)
info_path = 'data/info'
info_path = os.path.join(home_path, info_path)

data_list = os.listdir(data_path)
train_list = [l for l in data_list if 'train' in l and l.endswith('.txt')]
test_list = [l for l in data_list if 'valid' in l and l.endswith('.txt')]
train_list.sort()


#train_list = train_list[7:]
#print train_list
'''
for train in train_list:
    stories_dir = train.strip('.txt').replace('.','_')
    story_prefix = stories_dir
    stories_dir = os.path.join(data_path, stories_dir)
    if not os.path.exists(stories_dir): os.makedirs(stories_dir)
    
    with codecs.open(os.path.join(data_path, train), 'r', encoding='utf-8') as f:
        lines = f.readlines()
        lines = [json.loads(l.strip()) for l in lines]

        for l in lines:
            story_name = os.path.join(stories_dir, '%s_%07d.story' % (story_prefix, l['id']))
            with codecs.open(story_name, 'w',encoding='utf-8') as writer:
                writer.write(l['content'] + '\n\n')
                writer.write('@title\n\n' + l['title'])

        
        print train, 'done'
        print 'num of stories: %d' % len(lines)
''' 

print test_list
for test in test_list:
    stories_dir = test.strip('.txt').replace('.','_')
    story_prefix = stories_dir
    stories_dir = os.path.join(data_path, stories_dir)
    if not os.path.exists(stories_dir): os.makedirs(stories_dir)

    with codecs.open(os.path.join(data_path, test), 'r', encoding='utf-8') as f:
        lines = f.readlines()
        lines = [json.loads(l.strip()) for l in lines]

        for l in lines:
            story_name = os.path.join(stories_dir, '%s_%07d.story' % (story_prefix, int(l['id'])))
            with codecs.open(story_name, 'w',encoding='utf-8') as writer:
                writer.write(l['content'])

        print test, 'done'
        print 'num of stories: %d' % len(lines)


