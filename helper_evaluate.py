import torch 
import numpy as np
import random
import os

def set_all_seeds(seed):
    os.environ["PL_GLOBAL_SEED"] = str(seed)
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)

def test(model, test_loader, n_way, device):
  correct = 0
  count = 0
  model.eval()
  with torch.no_grad():
    for batch_idx, (main_img, test_set, target) in enumerate(test_loader):
      main_img = main_img.to(device)
      target = target.to(device)
      pred_val = 0
      pred = -1
      for i, test_img in enumerate(test_set):
        test_img = test_img.to(device)
        output = model(main_img, test_img)
        if output > pred_val:
          pred_val, pred = output, i
      if pred == target:
        correct += 1
      count += 1
      if count % 20 == 0:
        print("Accuracy on {} way: {}".format(n_way, correct/count))
