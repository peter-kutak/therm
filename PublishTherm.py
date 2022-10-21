from Publish import Publish

class PublishTherm(Publish):
  def __init__(self):
    super().__init__("therm")
    self.msgPattern=("[{{ "
            "\"bn\": \"myhome/therm/\""
            ",\"bt\": {}"
            "}},{{"
            "\"n\": \"temp\","
            "\"v\": {},"
            "\"u\": \"degC\""
            "}}]")


  def publish(self, temp):
    super().publish(temp)

