# from ploting.models import Poll, Choice, Vote
# from model_report.report import reports, ReportAdmin

# class PollModelReport(ReportAdmin):
#     title= _('All In one Report')
#     model=Poll
#     fields=[
#         'question',
#         'ceated_by',
#         'pub_date'
#     ]
#     list_order_by = ('pub_date')
#     type='report'

#     reports.register('poll-report', PollModelReport)