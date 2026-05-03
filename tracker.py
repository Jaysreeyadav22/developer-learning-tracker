      
from abc import ABC, abstractmethod


class BaseEntry(ABC):
    @abstractmethod
    def display(self):
        pass
    


class Topic(BaseEntry):
    def __init__(self, name , status):
        self.name = name
        self.status = status

    def display(self):
        emoji = self.get_status_emoji()
        return f'📚 Topic : {self.name} |  Status : {emoji} {self.status}'
    
    def get_status_emoji(self):
        if(self.status == 'Completed'):
            return '✅'
        elif(self.status == 'Pending'):
            return '⬜'
        elif(self.status == 'In Progress'):
            return '🔄'
    
class ProblemLog(BaseEntry):
    def __init__(self, date , problems_solved, difficulty):
        self.date = date
        self.__problems_solved = problems_solved
        self.__difficulty = difficulty

    
    def get_problems_solved(self):
        return self.__problems_solved

    def set_problems_solved(self, value):
        if value > 0:
            self.__problems_solved = value
        else:
            print("❌ Problems solved must be greater than 0!")

    def display(self):
        if(self.__difficulty == 'Easy'):
            difficulty_emoji = '🟢'
        elif(self.__difficulty == 'Medium'):
            difficulty_emoji = '🟡'
        elif(self.__difficulty == 'Hard'):
            difficulty_emoji = '🔴'
        return f'📅 Date: {self.date} | Problems Solved: {self.__problems_solved} | Difficulty: {difficulty_emoji} {self.__difficulty}'

class RoadmapTask(Topic):
    def __init__(self, name, status, deadline , priority):
        super().__init__(name, status)
        self.deadline = deadline
        self.priority = priority

    def display(self):
        emoji = self.get_status_emoji()
        if(self.priority == 'High'):
            priority_emoji = '🔴'
        elif(self.priority == 'Medium'):
            priority_emoji = '🟡'
        elif(self.priority == 'Low'):
            priority_emoji = '🟢'
        return f'🗺️  Task : {self.name} |  Status : {emoji} {self.status} | Deadline: {self.deadline} | Priority: {priority_emoji} {self.priority}'

class StudyTracker:
    def __init__(self, topics, roadmap_tasks , problem_logs):
        self.topics = []
        self.roadmap_tasks = []
        self.problem_logs = []

    def add_topic(self, topic):
        self.topics.append(topic)

    def add_problem_log(self, problem_log):
        self.problem_logs.append(problem_log)

    def add_roadmap_task(self, roadmap_task):
        self.roadmap_tasks.append(roadmap_task)
    
    def show_topics(self):
        print("\n===== 📚 TOPICS =====")
        for topic in self.topics:
            print(topic.display())
        
    def show_problem_logs(self):
        print("\n=====  💻 PROBLEM LOGS =====")
        for log in self.problem_logs:
            print(log.display())
    def show_roadmap_tasks(self):
        print("\n===== 🗺️ ROADMAP TASKS =====")
        for task in self.roadmap_tasks:
            print(task.display()) 

    def show_summary(self):
        completed_topics = sum(1 for topic in self.topics if topic.status == 'Completed')
        completed_tasks = sum(1 for task in self.roadmap_tasks if task.status == 'Completed')
        total_problems = sum(log.get_problems_solved() for log in self.problem_logs)
        percentage = (completed_tasks / len(self.roadmap_tasks) * 100) if self.roadmap_tasks else 0

        print("\n===== 📊 STUDY SUMMARY =====")
        print(f"\n📊 Topics: {len(self.topics)} total | {completed_topics} Completed ")
        print(f"💻 Problems Solved: {total_problems}")
        print(f"🗺️ Roadmap: {len(self.roadmap_tasks)} tasks  | {completed_tasks} Completed | {percentage:.0f}% done")

# Test abstraction
#class BrokenEntry(BaseEntry):
    


  

topic1 = Topic('OOP', 'Completed')
topic2 = Topic('Data Types', 'In Progress')
topic3 = Topic('Data Structures', 'Pending')
problemLog1 = ProblemLog('01-05-2026', 3, 'Easy')
problemLog2 = ProblemLog('02-05-2026', 2, 'Medium')
problemLog3 = ProblemLog('03-05-2026', 5, 'Hard') 
roadmap1 = RoadmapTask('OOP', 'Completed', '01-05-2026', 'High')
roadmap2 = RoadmapTask('Data Types', 'In Progress', '02-05-2026', 'Medium')
roadmap3 = RoadmapTask('Data Structures', 'Pending', '03-05-2026', 'Low')
tracker = StudyTracker(Topic, RoadmapTask, ProblemLog)
tracker.add_topic(topic1)
tracker.add_topic(topic2)
tracker.add_topic(topic3)
tracker.add_problem_log(problemLog1)
tracker.add_problem_log(problemLog2)
tracker.add_problem_log(problemLog3)
tracker.add_roadmap_task(roadmap1)
tracker.add_roadmap_task(roadmap2)
tracker.add_roadmap_task(roadmap3)
tracker.show_topics()
tracker.show_problem_logs() 
tracker.show_roadmap_tasks()
tracker.show_summary()
#broken = BrokenEntry()  
print(problemLog1.get_problems_solved())
problemLog1.set_problems_solved(-5)
problemLog1.set_problems_solved(10)
print(problemLog1.get_problems_solved())


