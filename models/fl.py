from turtle import forward
import torch
import torch.nn as nn
import torch.nn.functional as func

# calculation Multi-classification focal loss
class MultiFocalLoss(nn.Module):
    # alpha is prior weight of samples, gamma had better keep unchanged
    def __init__(self,alpha=[.2,.8],gamma=2) -> None:
        super(MultiFocalLoss,self).__init__()
        self.alpha = torch.tensor(alpha)
        self.gamma = torch.tensor([gamma])

        
    def forward(self,pred,y):
        # get pred label
        pred = torch.softmax(pred,1)
        # get ground truth
        label = y.item()
        # calculate focal loss
        fl_loss = -self.alpha[label]*(1-pred[0,label])**self.gamma*torch.log(pred[0,label])

        # turn to scalar
        return fl_loss.mean()

class BatchFocalLoss(nn.Module):
    def __init__(self,alpha=[.2,.8],gamma=2) -> None:
        super(BatchFocalLoss,self).__init__()
        self.fl = MultiFocalLoss(alpha,gamma)
        
        
    def forward(self,pred,y):
        floss = torch.FloatTensor([0])
        # iter all pred data and accumulate f-loss 
        for i in range(pred.shape[0]):
            flossi = self.fl.forward(torch.unsqueeze(pred[i],0),torch.unsqueeze(y[i],0))
 
            floss += flossi
        return floss