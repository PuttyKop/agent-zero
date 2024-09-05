from agent import Agent
from python.helpers import files
from python.helpers.print_style import PrintStyle

from agent import Agent
from python.helpers.tool import Tool, Response
from python.helpers import files
from python.helpers.print_style import PrintStyle

class TaskDone(Tool):

    def execute(self,args):
        self.agent.set_data("timeout", 0)
        return Response(message=self.args["text"], break_loop=True)

    def before_execution(self, args):
        pass # do not add anything to the history or output
    
    def after_execution(self, response, args):
        pass # do add anything to the history or output