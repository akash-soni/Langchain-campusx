[StateSnapshot(values={'topic': 'pizza', 'joke': 'What did the pepperoni say to the cheese on the pizza? \n\n"You wanna have a pizza me?"', 'explanation': 'This joke is a play on words, using "pizza" in two different ways. The pepperoni is asking the cheese if it wants to fight or have a confrontation by saying "You wanna have a pizza me?" as a pun on the phrase "You wanna have a piece of me?" This joke is humorous because it is unexpected and uses a common phrase in a clever and silly way.'}, next=(), 

config={'configurable': {'thread_id': '1', 'checkpoint_ns': '', 'checkpoint_id': '1f06dd18-1742-6001-8002-67b43dcc003e'}}, 
metadata={'source': 'loop', 'step': 2, 'parents': {}, 'thread_id': '1'}, created_at='2025-07-31T05:45:03.594905+00:00', parent_config={'configurable': {'thread_id': '1', 'checkpoint_ns': '', 'checkpoint_id': '1f06dd18-056a-66d7-8001-c0b0d5dfd5fa'}}, 

tasks=(), interrupts=()),
 


StateSnapshot(values={'topic': 'pizza', 'joke': 'What did the pepperoni say to the cheese on the pizza? \n\n"You wanna have a pizza me?"'}, 

next=('generate_explanation',), config={'configurable': {'thread_id': '1', 'checkpoint_ns': '', 'checkpoint_id': '1f06dd18-056a-66d7-8001-c0b0d5dfd5fa'}}, metadata={'source': 'loop', 'step': 1, 'parents': {}, 'thread_id': '1'}, created_at='2025-07-31T05:45:01.724027+00:00', parent_config={'configurable': {'thread_id': '1', 'checkpoint_ns': '', 'checkpoint_id': '1f06dd17-f202-6aa4-8000-a87860fa94a0'}}, tasks=(PregelTask(id='73ceccc1-c855-8ccb-f92a-b4e9831f268e', name='generate_explanation', path=('__pregel_pull', 'generate_explanation'), error=None, interrupts=(), state=None, result={'explanation': 'This joke is a play on words, using "pizza" in two different ways. The pepperoni is asking the cheese if it wants to fight or have a confrontation by saying "You wanna have a pizza me?" as a pun on the phrase "You wanna have a piece of me?" This joke is humorous because it is unexpected and uses a common phrase in a clever and silly way.'}),), interrupts=()),



StateSnapshot(values={'topic': 'pizza'}, 

next=('generate_joke',), config={'configurable': {'thread_id': '1', 'checkpoint_ns': '', 'checkpoint_id': '1f06dd17-f202-6aa4-8000-a87860fa94a0'}}, metadata={'source': 'loop', 'step': 0, 'parents': {}, 'thread_id': '1'}, created_at='2025-07-31T05:44:59.689232+00:00', parent_config={'configurable': {'thread_id': '1', 'checkpoint_ns': '', 'checkpoint_id': '1f06dd17-f1fb-6582-bfff-5744edc9147f'}}, tasks=(PregelTask(id='d119a925-834e-ca16-56c6-050ebd74bd1b', name='generate_joke', path=('__pregel_pull', 'generate_joke'), error=None, interrupts=(), state=None, result={'joke': 'What did the pepperoni say to the cheese on the pizza? \n\n"You wanna have a pizza me?"'}),), interrupts=()),



StateSnapshot(values={}, 

next=('__start__',), config={'configurable': {'thread_id': '1', 'checkpoint_ns': '', 'checkpoint_id': '1f06dd17-f1fb-6582-bfff-5744edc9147f'}}, metadata={'source': 'input', 'step': -1, 'parents': {}, 'thread_id': '1'}, created_at='2025-07-31T05:44:59.686233+00:00', parent_config=None, tasks=(PregelTask(id='b0cf7f4c-bd32-b357-e87c-0b7154787d5a', name='__start__', path=('__pregel_pull', '__start__'), error=None, interrupts=(), state=None, result={'topic': 'pizza'}),), interrupts=())]