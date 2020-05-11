from django import template
register = template.Library()

@register.filter
def trim(stringIn, separator):
  string = str(stringIn)
  return string.split(separator)[0]+'.' + string.split(separator)[1][:3]

@register.filter
def cutmiddle(string, number):
  return string[0:number] + '...' + string[len(string)-number:]
