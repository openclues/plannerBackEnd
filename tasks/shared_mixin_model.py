from django.db import models

from customuser.models import CustomUser


class SharedContentMixin(models.Model):
    APPROVED = 'approved'
    PENDING = 'pending'
    DISAPPROVED = 'disapproved'

    APPROVAL_CHOICES = (
        (APPROVED, 'Approved'),
        (PENDING, 'Pending'),
        (DISAPPROVED, 'Disapproved'),
    )

    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='%(class)s_sent_share_requests')
    receiver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='%(class)s_received_share_requests')
    created_at = models.DateTimeField(auto_now=True)
    is_approved = models.CharField(max_length=15, choices=APPROVAL_CHOICES, default=PENDING)

    def approve_and_share(self, shared_object):
        if self.is_approved == self.APPROVED:
            shared_object.shared_with.add(self.receiver)
        else:
            shared_object.shared_with.remove(self.receiver)  # Remove receiver if request is not approved

    class Meta:
        abstract = True
