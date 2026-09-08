"""Editorial changes to the existing guide's data. Preserve IDs and exercise facts."""

def apply(d):
    parts = [
        ('Foundations', 'Decide where AI belongs in your work.', 'Begin with your role, the tools, and the judgments that make a proposed use appropriate.'),
        ('Systems', 'Make the work easier to direct and review.', 'Develop prompts, organize sources, improve writing, and plan the steps of a larger assignment.'),
        ('Building', 'Improve a service and test a proposed tool.', 'Examine how the work reaches the client, then test a limited change before others depend on it.'),
        ('Leadership', 'Carry what you learn into your practice.', 'Keep useful methods and decide how the team should review, learn from, and take responsibility for the work.')
    ]
    for p, (name, title, desc) in zip(d['PARTS'], parts):
        p.update(name=name, title=title, desc=desc)
    # Original document titles remain in the bibliography; they no longer narrate the chapters.
    for source in d['SOURCES']:
        if source['id'] == 'fall':
            source.update(short='AI-enabled lawyering', note='Joe Regalia’s teaching framework for professional judgment, responsible use, workflows, building, and leadership. The public edition adapts the course framing for lawyers and law students.')
        elif source['id'] == 'student':
            source.update(short='AI foundations', note='Joe Regalia’s introductory teaching material. The public edition explains stable concepts without treating historical product names, statistics, or descriptions as current guarantees.')
        elif source['id'] == 'short':
            source.update(short='Responsible-use checklist', note='The before, during, and after checklist, four-minute self-assessment, and use-note pattern are adapted for professional and educational assignments.')
        elif source['id'] == 'slides':
            source.update(short='Writing and prompting', note='Joe Regalia’s workshop materials supply the collaboration practices and writing exercises. Original exercise passages retain their substantive facts. Client-branded slide images are not distributed in this guide.')
        elif source['id'] == 'graph':
            source.update(title='Mapping an AI-assisted workflow', short='Workflow teaching module', note='The fictional vendor assignment was developed for this guide. It illustrates work planning and review; it does not decide an actual termination dispute.')
    glossary = {
        'AI':'Artificial intelligence is the broad field of making machines perform tasks that appear to require intelligence. This guide focuses on systems used to work with language and legal assignments.',
        'Agent':'An agent can pursue an assignment through several actions, such as reading documents and preparing a comparison. Specify what it may access and where it must return for approval.',
        'API':'An application programming interface lets one software system communicate with another. A legal product may use one to send a task to an underlying model.',
        'Benchmark':'A benchmark is a defined test used to compare performance. A general score does not establish how a tool will handle your particular assignment.',
        'Context window':'The context window is the information a model can consider while generating a response. It has a capacity measured in tokens; important material may need to be supplied again in a continuing project.',
        'Divergence rule':'This is an exercise in independent thinking: make your own list, consider AI’s additions and objections, then develop another list that includes an approach the model did not offer.',
        'Embedding':'An embedding represents information numerically so software can compare meaning or similarity. Retrieval systems may use embeddings to find passages related to a question.',
        'Escalation':'Escalation means returning a question to a designated person. Specify the circumstance that requires it, such as a missing source that could affect the recommendation.',
        'Evaluation set':'An evaluation set contains examples used to test a tool or workflow. Include ordinary assignments and cases in which the correct response is to stop or ask for help.',
        'Few-shot prompting':'Few-shot prompting means supplying a small number of examples. Explain what they demonstrate. A request without examples is sometimes called zero-shot prompting.',
        'Fine-tuning':'Fine-tuning adds training to an existing model to adapt its behavior. Supplying a reference document during a task is different; it does not itself retrain the model.',
        'Foundation model':'A foundation model is trained on broad material and can support many applications. A particular legal product may combine it with specialized sources and software.',
        'Frontier model':'A frontier model is among the most capable general-purpose models at a given time. The label changes as systems develop and does not guarantee performance on a legal task.',
        'Generative AI':'Generative AI produces content, which may include text, code, images, or audio. Predictive AI instead classifies, scores, or forecasts information.',
        'Graph / workflow map':'A workflow map shows tasks and how their results pass to later steps. It can also show where missing information or required review changes what happens next.',
        'Guardrails':'Guardrails are restrictions intended to limit a system’s behavior. Find out whether a claimed restriction is a written instruction, a technical permission, or another control.',
        'Hallucination':'A hallucination is false or invented content in a generated response. In legal work, watch for subtle changes to a source’s meaning as well as fabricated cases or quotations.',
        'Handoff':'A handoff passes a task’s result to the next person or step. Include the source support and unresolved questions that the next reviewer needs to understand the result.',
        'Harness':'A harness is the supporting system around a model, including its tools, context, and controls. Organizing reference files helps with one part of that system; it does not enforce software permissions.',
        'Human approval point':'A human approval point requires a designated person to review work and decide whether it may proceed. A written request for approval does not itself implement a technical restriction.',
        'Inference':'In AI engineering, inference means running a model to produce output. In legal analysis, an inference is a conclusion drawn from evidence. The two meanings should not be confused.',
        'Internal risk':'Internal risk concerns how AI may narrow your attention or thinking before you have examined the problem yourself. It can matter even before anyone else relies on the output.',
        'External risk':'External risk concerns harm from the work or its use. Examples include advice based on a false fact or disclosure of information that should remain protected.',
        'Knowledge graph':'A knowledge graph maps relationships in information, such as connections among people, events, and documents. A workflow map instead describes how work should proceed.',
        'Knowledge cutoff':'A knowledge cutoff describes the limit of a model’s built-in training information. Newer material needs to come from supplied sources or connected tools; older information may still need verification.',
        'Large language model / LLM':'A large language model learns patterns in language and generates responses. An application may connect it to source retrieval and other tools to support a broader assignment.',
        'Machine learning':'Machine learning develops systems from patterns in data rather than relying only on rules written by a programmer.',
        'Model':'The model is the trained system that produces an output. Distinguish it from the application, sources, and permissions surrounding it.',
        'Multimodal':'A multimodal system can work with more than one kind of material, such as text and images. Check whether the particular application can read the material your assignment requires.',
        'Open weights':'Open weights are published model parameters that can be run in another environment, subject to applicable terms. Their availability does not establish that a deployment protects client information.',
        'Parameters':'Parameters are internal numerical settings adjusted during training. The learned patterns they represent are different from an accessible record of a source.',
        'Predictive AI':'Predictive AI classifies, scores, or forecasts information. Ranking documents by likely responsiveness is one example.',
        'Prompt':'A prompt is input that directs an AI task. It may include instructions, questions, examples, and material to work on. Explain the assignment clearly enough that you can judge the result.',
        'Prompt injection':'Prompt injection places instructions in material an AI reads in an attempt to redirect it. For example, a document might tell an agent to ignore the assignment or share unrelated information.',
        'Purposeful friction':'Purposeful friction means a planned pause or piece of human work intended to protect accuracy or judgment. The self-assessment before feedback is one example used in this guide.',
        'RAG / retrieval':'Retrieval-augmented generation finds source material and uses it to help compose an answer. Check both the selection of material and the interpretation that follows.',
        'Reasoning model':'A reasoning model is designed to spend additional computation working through a problem before answering. Judge the actual result rather than relying on the label.',
        'Regression test':'A regression test repeats a known test after a change. It helps reveal whether the revised system has become worse at something it previously handled.',
        'System prompt':'A system prompt supplies high-level instructions for model behavior. User-saved instructions may add guidance, but they do not necessarily control the application’s rules or permissions.',
        'Token':'A token is a small unit used to represent and measure model input or output. In text, it may correspond to a word, part of a word, or punctuation.',
        'Vibe coding':'Vibe coding commonly refers to building with natural-language instructions and AI-generated code. In this guide, begin with a limited prototype and test it before others rely on it.',
        'Work order':'A work order specifies an agent’s assignment, sources, permissions, and required results. It also states when the system must stop and which steps need human approval.'
    }
    for item in d['GLOSSARY']:
        if item[0] in glossary: item[1] = glossary[item[0]]
    d['GLOSSARY'].append(['Context engineering','Context engineering concerns which instructions, sources, and prior results a model receives for the next task. For a lawyer, a useful starting point is keeping the current assignment and reviewed findings clearly organized.','harness'])
    titles = {
        'preflight':('Decide whether to use AI','Apply the five questions to one proposed use and record what you need to resolve before proceeding.'),
        'pause':('Assess your work before feedback','Record your own view before asking for feedback, then return to explain what you would accept, change, or reject.'),
        'graph':('Follow the vendor-review workflow','Work through a fictional assignment and decide what should happen when the evidence does not establish receipt of notice.'),
        'promptbuilder':('Prepare a prompt for your assignment','Describe the work you need. The form assembles instructions you can review and copy into an approved AI tool.'),
        'workorder':('Write an assignment for an AI agent','Specify the work, permitted actions, required support, and decisions that must return to a person.'),
        'fee':('Revise the fee-table sentence','Try a revision, then examine how different verbs and structures affect the meaning and readability.'),
        'stonebridge':('Explain the Stonebridge dividend question','Reorganize the advice so the reader understands why permission cannot yet be confirmed and what support is needed.'),
        'falcon':('Explain the Falcon disclosure question','Clarify the proposed disclosure while preserving both the NDA concern and the question of unnecessary information.'),
        'aiisms':('Edit a deliberately generic paragraph','Identify the writing and analytical problems before examining the prepared annotations.'),
        'process':('Plan a change to a legal process','Describe how the work happens now, identify a problem, and prepare a limited change to test.'),
        'shipping':('Review a tool before people rely on it','Record the tests, reviews, and unresolved questions relevant to a proposed pilot.'),
        'reflection':('Revisit a question about legal practice','Keep an initial view and return after experience gives you something new to consider.'),
        'priorities':('Choose what to investigate first','Read the employee-departure facts and explain your priorities before considering other approaches.'),
        'playbook':('Keep a playbook of useful methods','Record what you learned from an assignment, including the instructions, checks, and limits that matter when reusing the method.')
    }
    for lab in d['LABS']:
        lab['title'], lab['desc'] = titles[lab['id']]
    for prompt in d['PROMPTS']:
        prompt['source'] = prompt['source'].replace('Semester checklist','Responsible-use checklist').replace('Fall guide','AI-enabled lawyering').replace('Skills & AI-isms','Writing and prompting workshop')
    for key in ['STONEBRIDGE','FALCON']:
        number=56 if key=='STONEBRIDGE' else 57
        d[key]['source']=f'The original practice passage is from Joe Regalia’s writing and prompting workshop, slide {number}. The sample revision and review questions were developed for this guide.'
    d['FEE_OPTIONS'][0]['note']='This version replaces some words but keeps the indirect description of the table’s purpose. Consider whether “aims to help” and “comprehend” make the relationship easier to understand.'
    d['FEE_OPTIONS'][1]['note']='“Informs” gives the sentence a more direct verb. Read closely, though: the original distinction between costs borne directly and indirectly is no longer explicit. A shorter sentence must still convey the intended information.'
    d['FEE_OPTIONS'][2]['note']='“Shows” describes what the table does, while the sentence preserves direct and indirect costs. This is one possible revision. Judge whether it fits the surrounding document and its reader.'
    d['AIISM_LENSES'][0]['explain']='The highlighted language announces importance without explaining the problem. “Multifaceted challenge” leaves the reader to discover which question matters. Replace the phrase with a supported point, or identify the information needed to make one.'
    d['AIISM_LENSES'][1]['explain']='The repeated transitions and artificial contrast make different ideas sound mechanically similar. “May potentially support” also adds a hedge without explaining the uncertainty. Decide how each sentence should advance the analysis and name what remains unresolved.'
    d['AIISM_LENSES'][2]['explain']='The paragraph gives similar space to several concerns without showing which deserves attention first. Decide what the reader needs to know before choosing paragraph breaks or headings. Formatting should reveal the reasoning rather than impose a pattern on it.'
    d['AIISM_LENSES'][3]['explain']='The passage never identifies the controlling authority or explains how the facts support a particular next step. Removing conspicuous words will not supply that analysis. Name the unanswered question and the source or investigation needed before making a recommendation.'
    # These historical field IDs are intentionally unchanged for backup compatibility.
    g=d['RESOURCE_GUIDANCE']
    g['pause'].update(result='You will have your own assessment to compare with feedback from an approved tool, a colleague, or a later review.',after='After receiving feedback, return to explain why an important suggestion should be accepted, changed, or rejected.')
    g['reflection'].update(need='Choose a question you can connect with your experience. No other preparation is required.',first='Write your current view, then return after a matter, course, workshop, or experiment gives you something new to consider.',result='You will have an initial response and space to revisit it twice. There is no required timetable.',after='Return when you have something to add. Explain what affected your view, or why you still hold it.',steps=['Choose a question and record your initial view.','After relevant experience, use the next space to explain what you learned.','Return again when useful. Each question keeps its own responses, so changing the selection does not erase earlier work.'],save='Responses save separately for each question in this browser. They are not submitted to Write.law, an instructor, or an employer.')
    g['playbook'].update(need='Bring an experience worth learning from. You can begin with one area and return to the others later.',first='Describe a method, decision, or failure and what you learned from it. Include enough context to judge when the lesson applies.',result='You will have a record that helps you decide how to handle a similar assignment. This is separate from the page that collects your individual notes.',after='Test the method again when the work calls for it. Add the exception or revision that the next experience reveals.')
    for entry in g.values():
        for key,value in list(entry.items()):
            if isinstance(value,str):
                entry[key]=value.replace('a classmate','a colleague or classmate').replace('your instructor','your instructor or workshop leader')
    area=d['AREA_HELP']
    area['home'].update(title='Where should I begin?',tip='Choose an explanation, a supplied exercise, or a form for your own assignment.',body='<p>For an introduction, begin with the first chapter. For a particular task, use the suggested routes on the homepage or search the guide.</p><p><strong>Chapters</strong> explain the methods. <strong>Exercises</strong> supply a problem and prepared discussion. <strong>Templates & worksheets</strong> help you plan an assignment or prepare instructions to use elsewhere. <strong>My saved work</strong> collects what you have written.</p>')
    area['chapters'].update(body='<p>The four parts organize the subject matter. Foundations covers your role and responsible use. Systems develops the methods for prompting, writing, organizing sources, and supervising work. Building addresses process improvement and testing. Leadership helps you carry those lessons into practice.</p><p>Read in order or choose a chapter for the task in front of you. An activity inside a chapter is the same activity available on its own page, with the same saved response. Marking a chapter as read records your progress; it is not a grade.</p>')
    area['exercises'].update(body='<p>Each exercise supplies a passage or fictional problem. Read the instructions, make your own attempt, then open the comparison or discussion. You do not need an AI account.</p><p>The explanations are prepared teaching material, not generated feedback about your answer. Use them independently or alongside a course or workshop. Any required submission happens outside this guide.</p>')
    area['notebook'].update(body='<p>Your notes, forms, and exercise responses save in this browser profile. They are not sent to Write.law, an instructor, or an employer. Another device, browser, or site address has separate storage.</p><p>Download readable notes to review or share them. Download a backup to restore the saved state elsewhere. Restoring a backup replaces the work in the destination browser, so first keep a copy of anything you need.</p><p>Use only non-sensitive material. Other people using the same browser profile may be able to see the entries, and clearing browser data can remove them.</p>')
    area['glossary'].update(body='<p>Search a term or a word in its explanation. Each entry links to a chapter where you can see the idea used in legal work.</p><p>You do not need to memorize the vocabulary before beginning. Use the glossary when a term gets in the way of understanding the task.</p>')
    area['sources'].update(title='Where the teaching comes from',tip='Read the teaching sources and the notes distinguishing practice examples from legal authority.',body='<p>The guide develops Joe Regalia’s teaching materials for Write.law lawyers and law students. Source notes retain the original document titles and page references.</p><p>Practice passages, prepared revisions, and the fictional workflow are distinguished from primary legal and technical references. Product descriptions are not recommendations or assurances about a particular account.</p>')
    # These are descriptions, not approval statuses or factual assertions about a user's matter.
    d['CHECKLIST']=[
      ['Before opening a tool',['Check whether the particular use is permitted.','Confirm that the system is appropriate for the information.','Develop enough of your own understanding to direct the task.','Identify the consequences of error and how you will review the result.']],
      ['While working with it',['Give the system a defined assignment.','Supply appropriate sources and examine important support.','Ask questions that help you develop or challenge the work.','Limit permissions and keep required approval with the designated person.']],
      ['Before relying on the result',['Complete the substantive checks the use requires.','Decide what to accept, change, or reject.','Keep a record and disclose the use when required.','Continue practicing the underlying skills without AI.']]
    ]
    # Preserve the exercise passages, numbers, comparisons, question ordering, and all saved IDs.
    return d
