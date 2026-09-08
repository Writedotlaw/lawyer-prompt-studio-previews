"""Reading-first editorial changes, grounded in the four supplied teaching sources.
Every key is an existing chapter and section, preserving previously shared links.
"""
PATCHES = {}
APPEND = {}
def replace(chapter, section, heading, text):
    PATCHES.setdefault(chapter, {})[section] = {'h':heading, 'markdown':text.strip()}
def add(chapter, section, text):
    APPEND.setdefault(chapter, {})[section] = text.strip()

replace('lawyer',0,'AI changes what we can do with legal knowledge.',r'''
Law is made of language. We read it to find out what happened, work through what the rules require, and explain what someone should do. For a long time, our technology helped us find and move the words. Now it can help produce them, including the analysis and argument those words contain.

That gives lawyers much more to consider than how quickly we can finish a first draft. We can explore an argument we would otherwise have set aside for lack of time. We can ask a patient tutor to explain unfamiliar technical material, compare several ways of presenting an issue, or build a small tool around a recurring client problem. My interest in AI begins with that wider opportunity: what could we do better, or do for the first time, if the work were easier to explore?

But everyone can ask a system to produce an answer. A lawyer's contribution has to extend beyond the request. We need to understand the problem well enough to decide whether the answer helps, which questions it misses, and what the person receiving it can reasonably do with it. Our writing and analytical skills therefore remain part of the method, even when a tool performs more of the production.

This guide brings those questions together. Foundations concerns our role, independent judgment, and responsible use. Systems develops the skills and processes for working with AI. Building examines how legal insight can become a better service or a tool. Leadership asks how we should manage the work and shape the profession as those possibilities change. You can read the chapters in order or return to a particular subject when your work calls for it. The explanations stand on their own; exercises and worksheets are optional companions.

Consider a client who asks whether it can terminate a software contract. Before asking AI to analyze the agreement, find out why the client wants out. Repeated outages may be interrupting its business. It may have found a cheaper alternative. Or it may prefer to keep the vendor if the relationship can be repaired. Those are different problems, even when they begin with the same legal question.
''')
replace('lawyer',1,'The lawyer turns uncertainty into a decision someone can use.',r'''
I describe the lawyer's job as converting legal uncertainty into responsible action for people and institutions. That description includes the answer, but it also includes the work that makes the answer worth acting on.

We **frame** the problem by distinguishing the client's objective from the question first presented to us. We **judge** among imperfect options, weighing the law alongside timing, cost, relationships, and consequences. We **design** how the work will get done so that a useful analysis can become a dependable service. Those responsibilities may send us back to the beginning of an assignment. Learning that the client cannot tolerate a service interruption, for example, changes what deserves attention in the termination analysis.

We also **counsel** the person behind the facts. A recommendation can be legally available and still wrong for someone who cannot bear its practical consequences. We **challenge** the emerging answer by examining assumptions, adverse support, and objections that deserve a hearing. Finally, we **own** the work we approve. We should be able to explain what was sent, filed, advised, or built, including the uncertainty that remains.

These are not six jobs performed in a fixed order. They overlap within a matter. You may counsel the client, discover a different objective, revise the research assignment, and then reconsider an earlier recommendation. AI can help you investigate each question, but a well-written response does not tell you that you asked the right question in the first place.
''')
add('lawyer',2,r'''
The expanded role also includes project management: sequencing work, allocating responsibility, and keeping deadlines, budgets, and dependencies visible. A team needs to know which finding the next task depends on and who can resolve a question when the source is incomplete. As an AI-agent manager, you make the same decisions about a system that may take several steps before returning to you.

A lawyer can also become a builder without first becoming a software engineer. Legal knowledge helps identify the problem, translate a rule and its exceptions into requirements, and devise tests that expose a bad answer. Working with technical experts remains important where the proposed use calls for expertise you do not have. The contribution is knowing what the tool should accomplish and what evidence would establish that it does.

Leadership connects these roles. Someone decides whether a faster process will mean more time to counsel clients, lower costs, better service, or only a higher volume of output. Someone also needs to protect junior lawyers' development when the tasks that once taught a skill are shortened or automated. Those decisions belong in our discussion of AI, not outside it.
''')
replace('lawyer',4,'Look beyond making the existing task faster.',r'''
My workshop materials describe three broad opportunities. The first is improving work you already do. A lawyer can use AI to examine a heading, develop another way to explain an exception, or find the places where a paragraph skips part of the analysis. The task remains recognizable, but you have more ways to improve it.

The second is making a useful process repeatable. An editing checklist can become a sequence that identifies potential issues, preserves their locations, and brings them back for a lawyer's review. A source collection, annotated examples, and recorded decisions can make the next assignment easier to begin. The time saved is only part of the benefit. A repeatable process can also make previously invisible decisions easier to inspect.

The third is attempting work you previously could not justify. You might explore several theories before choosing which deserve investigation, study a set of public opinions for recurring approaches to a question, or prototype a service for clients whom a traditional delivery model does not reach. These are possibilities to investigate, not assurances about what a particular model will do. A pattern in a judge's opinions, for example, is material for analysis; it cannot establish how that judge will decide the next case.

Across all three, the important unit is often a contribution within the larger task. You can seek alternatives while researching, feedback while outlining, and a specific comparison while editing. You do not have to hand over the whole matter to get substantial value from assistance. The following chapters develop the judgment needed to choose those contributions and use them well.
''')

add('basics',0,r'''
It also helps to distinguish training from use. During training, the model's parameters are adjusted as it learns patterns from data. When the model responds to a request, it is running with those learned parameters; this is called inference in AI engineering. A response may also use material supplied at that moment. Providing an opinion for an assignment is therefore different from training the model on that opinion.

Describing the foundation as prediction does not capture everything a finished product can do. A system may have additional training and tools that let it work through several tasks, retrieve material, and check intermediate results. Evaluate that finished system. Neither calling it “autocomplete” nor calling it “reasoning AI” tells you whether it can perform the particular legal work you have in mind.
''')
replace('basics',3,'A few distinctions explain most of the vocabulary.',r'''
**Retrieval-augmented generation**, often called **RAG**, combines finding material with generating an answer from it. A research product might retrieve cases; a document tool might find provisions in your agreements. Finding relevant material and interpreting it are separate jobs. A useful result needs both. The source collection also matters: a beautifully written account of the wrong documents does not answer the assignment.

A **reasoning model** is designed to devote additional computation to working through a problem. That can be useful for a multi-step question, but the product label is not a substitute for examining its answer. A displayed reasoning summary is something to review, not evidence that the reasoning or result is correct.

An **agent** can pursue a task through several actions. It might search, read what it found, prepare a comparison, and decide which action to take next. This shifts some of your attention from a single response to the chain of work. You need to know what information and authority the system has and which decisions must return to a person.

An **API** lets software communicate with another system. A **multimodal** product works with more than one kind of material, such as text and images. **Open weights** refers to published model parameters that can be run elsewhere, subject to the applicable terms. **Fine-tuning** adds training to an existing model. These features answer different questions. None, on its own, establishes that a product protects information or is suitable for a client matter.

The [glossary](#/glossary) provides a fuller reference, including terms used in the original introductory guide. You do not need to memorize them. Use the distinction when it helps you ask a better question about the system in front of you.
''')
add('basics',4,r'''
There are two other reasons to test the actual task. First, responses can vary. That variability is useful when exploring alternatives and troublesome when you need consistent extraction. Second, capability can be uneven: a system may produce sophisticated prose yet mishandle a date or overlook a small qualification. Success on the harder-looking task does not establish competence on the easier-looking one.

Product categories are a more useful starting reference than an old list of version numbers. General assistants support conversation and broad drafting. Search and study tools organize answers around retrieved or supplied material. Legal research products add legal sources and research features. Practice platforms coordinate document work and workflows. Writing and citation products focus more narrowly on editing or connecting claims with support. A product may span several categories, so inspect what the relevant feature actually does. Historical product examples from the original guide are identified as such in the source notes rather than presented as a current buying guide.
''')

replace('permission',1,'Answer the five questions for the particular use.',r'''
**Is the use allowed?** Identify the assignment, workplace policy, court requirements, client agreement, platform terms, and applicable law that bear on the proposed task. Permission to use a product is not permission for every action or every category of information. In a course, the purpose of the assignment can impose a further limit even when the tool is available.

**Is the input safe?** Determine what information the task needs and whether the system is approved to receive it. Privileged, confidential, personal, sealed, and proprietary information should not be treated as interchangeable with a public opinion. Removing a name does not necessarily make a document appropriate to share. The answer needs to address the actual material and the authorized setting.

**What happens if the output is wrong?** Consider who would rely on it and what could follow. An error might distort a record, cause delay, disclose information, or contribute to a decision that is difficult to reverse. The possibility of correcting a draft before it leaves the office is different from discovering the same error after the client has acted.

**Can I verify it?** Name the source, record, test, or reviewer that will establish whether the important parts are reliable. “Someone will look at it” is not yet a review plan. If the task is beyond your ability to evaluate, narrow it or identify the necessary expertise before relying on the result.

**Should I do the first pass?** Ask what understanding you need to bring to the task and which skills the task is meant to develop. Reading the case, synthesizing the rule, and choosing priorities may be the work you most need to do before asking for help. The next chapter explains how the first pass can vary with the assignment.

The source guide groups uses into green, yellow, and red as a starting way to think about control. Green covers relatively low-stakes assistance you can evaluate, such as formatting or tone options after your own review. Yellow includes summaries, clause alternatives, and analysis that may influence formal work; these need active direction and substantive checks. Red includes restricted data in public tools, unverified law or facts in formal work, and unsupervised individualized advice. The source treats those uses as inappropriate unless authorized and highly controlled and verified. The colors do not approve the use. A supposedly minor edit can still alter meaning or expose information.
''')
add('permission',2,r'''
The distinction produces four different situations. Brainstorming can have little immediate external consequence but substantial thinking risk: an early menu can determine which questions you investigate. A first human list, AI expansion, and another human pass address that problem more directly than checking the eventual citations alone.

AI-first strategy or dispositive drafting can combine high thinking risk with high external risk. The source recommends avoiding those uses unless the work is highly controlled, grounded in a human first pass, and directed toward alternatives and challenges. At the other end, a non-substantive format change usually calls for engagement with the edited result rather than an elaborate strategy review.

Citation, quotation, and record-location checks may be less likely to choose your theory for you, yet errors in those tasks can have serious external consequences. They require a dependable checking process and human verification. These examples explain why “low risk” is incomplete unless we say which risk we are discussing.
''')
add('permission',3,r'''
The short guide identifies specific reasons to stop and ask: conflicting instructions, access beyond what the task requires, sensitive inputs, a material source that cannot be located or validated, a consequential use such as advice or filing, an unexplained material conclusion, or certainty that the facts and law do not support. A stop does not have to abandon the matter. It can return a focused question, identify the missing source, or restrict the next step to work that is authorized and checkable.
''')

replace('think',1,'Make your own assessment before receiving feedback.',r'''
Before feedback arrives, write down your current answer. Identify the strongest and weakest parts of the reasoning, the authority or fact still needing attention, and the kind of feedback that would help most. Those are the five questions in the four-minute pause from the short guide.

The value is the comparison that follows. A suggested revision may address a weakness you already recognized. It may reveal a problem you missed. Or it may sound convincing without answering the concern that matters. Mark an important suggestion as something to accept, modify, or reject, and give a reason. That small explanation makes your decision visible to you.

For example, suppose you believe the client's current evidence does not establish receipt of notice. A suggested opening says the cure period has expired. Your preliminary assessment gives you a reason to question the change immediately. Another response may identify a source you overlooked. You can then examine that source and explain why your view changed rather than treating the new answer's confidence as the reason.

Four minutes is a suggested practice, not an established threshold for legal performance. The short guide refers to research with science students and expressly notes that it does not establish the same effect in law school. Use the pause as a way to develop and compare your judgment. The optional worksheet provides a place to record the answers; the method does not depend on using the form.
''')
replace('think',2,'Different priorities can produce different investigations.',r'''
The employee-departure problem makes the importance of a first pass visible. Read the supplied facts as a worked example rather than a question with one established legal answer:

{{read:priority-facts}}

The response shown in the workshop foregrounds the export using the director's credentials, her message about taking the playbook, and her contact with former accounts. Those facts give the company a narrative worth investigating. But other facts point toward different questions. Another director sometimes used the credentials. The agreement permits customer-initiated business. The company delayed before filing, and the requested relief is broader than a ban on soliciting identified customers.

A lawyer might therefore begin with attribution, the contractual exception, the urgency of the requested relief, or its breadth. Each priority changes the next assignment. A focus on attribution calls for evidence of who used the account. A focus on the exception calls for better evidence of who initiated contact. A focus on the requested order asks how its scope connects with what the company can establish.

I have used this hypothetical with lawyers and judges, and their priorities vary. That disagreement matters because AI can present a selected ranking as though the assignment had a natural starting point. Your task is to examine the ranking, not accept it as a substitute for deciding what matters. The supplied packet has no controlling law that resolves the dispute, so neither the workshop's response nor this discussion establishes who should win.
''')
add('think',3,r'''
The longer source guide calls this a **divergence rule**: produce an initial human list, ask AI to expand and challenge it, and make a second human list containing at least one approach the model did not supply. The point is to protect room for a different idea after an apparently complete answer arrives.

The same guide describes other forms of purposeful friction. Ask for an adverse authority, a skeptical reader's objection, or an implementation failure before settling on a recommendation. Treat unsupported propositions as hypotheses until they have reviewed support. Create distance between generation and consequential reliance through a fresh-reader pass, another lawyer, or a later verification session. Record where your judgment changed the response. Each step protects something particular; it is not extra process for its own sake.
''')

add('ethics',0,r'''
It helps to give each duty an operational meaning. Confidentiality affects data selection, access, retention, and the environment you use. Communication affects what the client needs to know under the rules, agreement, and circumstances. Supervision affects policies, training, responsibility for review, and the point at which work may proceed. Independent judgment calls for practical, economic, moral, social, and human considerations alongside the law. A system can help gather or explain those considerations without deciding their relative importance for the client.
''')
replace('ethics',4,'Direction from someone else does not settle your responsibility.',r'''
A supervising lawyer asks for an AI-generated case summary before you have opened the opinion. The client may act on it that afternoon. The problem is not solved by noting who requested the summary. You still need to identify what has and has not been checked and what can responsibly be sent.

The source guide points to Model Rule 5.2 for the principle that a subordinate lawyer remains bound by professional rules despite another person's direction. The full rule also addresses a supervisory lawyer's reasonable resolution of an arguable question of professional duty; applying it requires the actual rule and the relevant facts. This example does not resolve a jurisdiction-specific professional-responsibility question.

The practical communication should explain the unresolved issue and the proposed next step. You might tell the supervisor that the holding has not yet been checked, describe the review you can complete, and distinguish any interim status report from advice based on the unchecked summary. The same discipline applies when an instructor, client, or system presses for an answer that exceeds what you can support.

An accurate use note cannot cure inadequate review. It records what you did and what you relied on. The work must still meet the substantive standard for its intended use.
''')

replace('method',0,'Build the exchange around six working practices.',r'''
Good prompting begins with how you do the work. A request cannot supply a priority you have not chosen or a standard of good writing you cannot recognize. My six working practices connect your own contribution with the kinds of assistance AI can offer.

### First, do some work.

The first pass gives you a view to compare with the response. For a sentence, identify what makes it difficult to read. For an outline, decide what the reader needs explained and which issues matter most. For analysis, develop enough of the rule and facts to recognize a useful challenge. The amount varies; the reason stays the same. You need a basis for directing and evaluating the contribution.

### Direct with guidance and examples.

Describe what should improve, supply the context, and show a useful example. A heading might work because it states a complete proposition, identifies who acted, and connects the action with the legal point. Tell the system that. Otherwise, “make it persuasive” leaves it to invent your standard, and “write like this” leaves it to choose which features of the sample to copy.

### Choose with options and iterations.

Ask for alternatives that expose a decision. Different openings can begin with the client's objective, the decisive fact, or the consequence of an unresolved condition. Compare the emphasis and the cost of each choice. Then identify what the next round should preserve and what it should change. The first response becomes material for further work rather than a finished answer you must either accept or discard.

### Lean on expansion, pressure testing, and identification.

These are different assignments. Expansion asks what else might matter or support an idea. Pressure testing asks what a strong opponent, skeptical judge, or affected client would say against it. Identification asks the system to locate a specified feature: sentences containing several ideas, unexplained jargon, unsupported steps, or passages where the reader may lose the thread. You can ask for this work without requesting replacement prose.

### Scale the work for yourself and the AI.

A large request can overwhelm the review as well as the generation. If the system reorganizes, rewrites, and adds analysis across ten pages, you have to detect several kinds of change at once. A defined issue, paragraph, heading, or source comparison may give you a more useful unit. Keep connected questions together when separating them would distort their relationship. The aim is a manageable amount of work, not the smallest possible prompt.

### Prompt in a way that incorporates those decisions.

The final request should reflect the choices that this task needs. It may include your first attempt, the relevant sources, a sample with an explanation, and a request for alternatives before drafting. Another task may need only a focused comparison and a clear limit. The practices are a way to conduct the work, not a requirement to write six messages or fill six boxes every time.
''')
add('method',1,r'''
Ask for the pros and cons of the alternatives, but examine those explanations too. A model may call every version “clearer” without identifying what actually changed. Press for a contrast you could disagree with: one version foregrounds uncertainty, another identifies the next action sooner, and a third gives more factual context before the recommendation. Now you have a decision to make.

You can also request alternatives to an analytical frame. After reading an opinion, explain the rule you think matters and ask which other rules or distinctions deserve consideration. After developing an argument from a particular passage, ask what other language or facts could bear on that argument. The workshop's research examples use assistance repeatedly within the process, rather than once at the beginning of research and once at the end of drafting.
''')
add('method',2,r'''
A useful follow-up can preserve a small writing success. “The verb here works, but the subject is vague” is enough to direct the next round toward a specific problem. You may also combine parts of two options, ask for a different emphasis, or stop revising because the passage already does its job. Producing another version is not an improvement by itself.
''')
replace('method',4,'Keep the five-stage process distinct from the six practices.',r'''
The **responsible-use operating system** in the longer source guide describes the whole assignment. Its stages have different jobs from the six practices for conducting an exchange.

The **human-first frame** establishes the objective, issues, decision points, and initial theory before the model supplies them. **AI-assisted expansion** develops that starting work through alternatives, comparison, structure, simulation, critique, or authorized drafting. The **lawyer-grade audit** examines authority, quotations, facts, procedural posture, reasoning, instructions, data handling, and the strongest counterargument. It is broader than confirming that citations exist.

**Human revision and judgment** is where you accept, reject, combine, and rewrite, then decide what should be used and why. **Document and improve** records the purpose, sources, significant output, checks, rejected suggestions, and process lesson when the assignment or risk warrants it. A useful lesson should change the next workflow rather than remain buried in a chat.

The five-question before-use check comes earlier: it asks whether the use is appropriate at all. The ten prompting principles in the next chapter help specify an individual assignment. The agent work order makes a longer delegation explicit. These frameworks do not compete for the same role. The guide explains each where it is useful so you can choose the one that addresses the decision in front of you.
''')

replace('prompting',1,'Use the ten principles to explain the assignment.',r'''
I use ten prompting principles to explain the choices behind a useful request. Each addresses a practical source of misunderstanding. They are choices to make when the task calls for them, not a fixed format that every request must follow.

### 1. Provide the role and audience.

Identify the perspective that would help and the person who needs the result. A skeptical reviewer has a different job from a client counselor. A client unfamiliar with a doctrine needs a different explanation from a specialist. A grand title does not create expertise; the useful part of the role is the assignment it clarifies.

### 2. Provide context, data, and goals.

Explain what the work should accomplish, which facts and documents matter, and what you have already decided. A summary intended to orient a new colleague may differ from one prepared to evaluate a single contractual condition. State the primary goal and any secondary goal whose tradeoff needs attention.

### 3. Use annotated examples.

Supply an example and explain the choice that makes it useful. It may use a concrete subject, put the answer before the background, or preserve a difficult qualification without burying the point. Say which features should transfer and which facts or wording must stay behind.

### 4. Use menus, expansion, and pressure testing.

A menu of meaningful options gives you alternatives to judge. Expansion can reveal an omitted reason, issue, or explanation. Pressure testing challenges the position with the best available objection. Ask for supporting material where the suggestion depends on facts or law. An invented counterargument is not more useful because it sounds forceful.

### 5. Set parameters for the result.

Describe the form that will help you use and check the response. You may need a source-linked table, a paragraph of advice, or headings that each state a proposition. Include the necessary scope and level of detail. A word count may constrain a task, but it does not explain what information deserves the space.

### 6. Iterate with follow-ups.

Tell the system which parts you accept and which need another round. “Keep the opening, but put the missing factual condition beside the recommendation” preserves a useful choice while directing a change. Avoid restarting the whole task when only one part is unresolved.

### 7. Break down the steps and stay organized.

When one task needs a reviewed result from another, state that sequence. For example, extract a source's relevant proposition, compare it with your intended use, and only then draft a heading. The useful result is observable intermediate work you can examine. You do not need to treat a displayed account of the model's internal reasoning as evidence of correctness.

### 8. Use AI to help improve your prompts.

Describe a result you liked and why, then ask for reusable instructions that would pursue those features on another assignment. Or ask the system to identify ambiguity in your proposed request before starting. Review the resulting prompt yourself. The system can make your unstated assumption more polished without making it right.

### 9. Reset and reuse.

Keep instructions that worked alongside the source requirements, examples, and limitations that made them useful. For a new matter, replace the old facts and confirm the applicable scope. In a long exchange, a fresh start with an accurate continuation record may be better than repeatedly appending qualifications to outdated directions.

### 10. Avoid AI-isms.

Give positive direction as well as identifying habits to avoid. Explain the audience, desired emphasis, and useful examples. Ask for connected prose where reasoning needs development, familiar words where jargon adds nothing, and substantive engagement with the facts. Removing conspicuous vocabulary will not supply a missing analysis; the editing chapter develops that distinction.
''')
replace('prompting',3,'Choose the variables that matter to this task.',r'''
A useful reusable prompt leaves the changing parts visible. Audience, primary and secondary goal, tone, format, examples, and limits may all vary. Do not preserve an old request's four-bullet structure merely because it once worked for a different email.

Describe priorities explicitly. When readability and a material qualification pull in different directions, say that the qualification must survive and ask for ways to explain it more clearly. At the end of a long request, a brief restatement of the main objective can help keep your own instructions coherent. That is an organizing habit, not a guarantee that the system will follow every direction.

Give quoted material a defined role. Tell the tool whether a passage is source evidence to preserve, a draft to revise, or a style example whose facts do not belong in the new work. In legal writing, specify that quotations and citations must not be silently altered. Quotation marks alone are not a reliable substitute for those directions.

The workshop also suggests making stylistic preferences explicit. Its example uses weighted traits and numerical targets for directness or sentence length. Treat those as possible prompt variables, not a formula for good writing. For this guide, the more useful instruction is to vary the rhythm naturally, explain the reasoning in full sentences, and let the material determine the paragraph. A repeated short–short–long pattern would defeat that aim.

Here is a prepared request that combines several of these choices without making the form the point:

```prompt
Revise the client email below using only the supplied information. The client needs to decide whether to provide the missing support before Friday. Put that decision and the reason near the beginning. Preserve the distinction between a condition we cannot yet confirm and a condition that has failed.

Offer two versions that organize the explanation differently. Explain what each helps the reader see and flag any change that might affect meaning. Use connected paragraphs, not a list unless the information genuinely needs one. Keep the quoted contractual language unchanged.

Email and source material: [supply the permitted material].
```

This example was prepared for the guide. It illustrates the workshop's instruction choices; it does not add a new factual record or establish the right recommendation in a live matter. The optional prompt builder helps organize the same choices for an assignment you bring.
''')
add('prompting',4,r'''
A proposed self-check can also ask for verification questions that would expose an error, answers grounded in the supplied material, and a revision addressing the resulting problems. Keep the distinction between critique and verification clear. The model's ability to ask and answer its own questions can expose something worth checking; it does not independently establish the answer.
''')

replace('graphing',2,'Follow the reasoning from the sources to the recommendation.',r'''
The map begins with the lawyer's objective. It then separates contract review from factual review, brings the findings together, and returns the important decisions to the lawyer. Here is the complete sequence in readable form:

{{read:workflow}}

The first two reviews can begin separately because they answer different initial questions. The contract task identifies the applicable requirements; the record task establishes what the available evidence shows. The comparison needs both results. Drafting needs the reviewed comparison and the lawyer's chosen approach.

Suppose the correspondence shows an email sent on June 4 but does not establish receipt. The comparison should identify a material gap because the fictional contractual period runs from receipt. It should not insert June 4 into the calculation merely because that is the only date available. The lawyer might seek an acknowledgment, ask for additional evidence, or approve a recommendation that expressly preserves the uncertainty. Those choices are different from a finding that the period has expired.

Later, an acknowledgment of receipt arrives. The timeline can be updated, the comparison reconsidered, and the recommendation revised. The new date does not automatically establish that every other contractual condition is met. It also does not count as the lawyer's approval. This is why the map separates new information, analysis, and authorization to proceed.

The interactive demonstration lets you move through the same sequence, but the reasoning above is the lesson. A workflow is useful when it makes necessary work and decisions visible, not merely because the diagram looks orderly.
''')
add('graphing',6,r'''
Several arrangements recur. A sequence handles work that must follow earlier work. Separate reviews that later come together can give a comparison distinct findings to examine. A branch changes the next action based on what the earlier task found. A return path sends a draft back when a source check identifies an overstatement. The vendor example uses all of these without requiring a complicated system.

A map of work is also different from a knowledge graph. A knowledge graph represents relationships in information, such as connections among people, events, and documents. A workflow map represents the tasks and decisions through which work proceeds. Both can be useful, but drawing one does not create the other.
''')

add('harness',0,r'''
The source materials use *harness* in two related senses. One describes the software surrounding a model, including tools, memory, retrieval, and enforced controls. Another describes a working arrangement of instructions, files, examples, and checks that you organize for an assignment. A folder of references can improve that working arrangement. It does not by itself implement the permissions and enforcement features of software. When planning a use, specify which part you have actually built.
''')
add('harness',1,r'''
The source guide identifies ten elements worth organizing. **Objective** and **context** explain the job and the circumstances. A **trusted source set** defines the materials, and **examples** show the intended standard and common mistakes. **Output structure** makes the result easier to inspect. **Sequence** identifies the tasks and their dependencies.

The remaining elements protect continued use: **independent checks**, **escalation rules**, **logs and versions**, and an **evaluation set**. A calculator, a source comparison, or a designated reviewer may perform different checks. Stop conditions return specified problems to a person. A version record identifies the instructions and sources used. Known-answer and boundary examples let you test whether a change improves the process or damages something that worked.

These elements need not become ten files. What matters is that the functions are covered. In the vendor matter, the requirements table and timeline preserve the source support. A record of unresolved issues tells the drafting task what it may not assume. A small set of receipt scenarios tests whether the workflow treats missing evidence appropriately. Each item has a job beyond making the folder look organized.
''')

replace('agents',1,'A work order makes the delegated decisions visible.',r'''
Before launching an agent, write the assignment as though you were delegating to someone who has no matter context unless you provide it. An **agent work order** makes that assignment explicit. Its twelve parts distinguish what the work should achieve from what the system may do to achieve it.

{{read:workorder}}

Notice the distinctions. The client outcome explains the decision the work should support. The deliverable describes what you need back. A quality standard describes how you will judge that result; an evidence requirement says what support must accompany it. Prohibited behavior identifies limits, while escalation triggers identify questions that need someone else's decision.

Human approval points also differ from tests. Approval is a decision in the actual assignment. A test asks how the proposed workflow behaves on an example before you rely on it. Keeping these subjects separate makes it easier to discover what a seemingly complete instruction has left unanswered.

The following excerpt shows those choices applied to the fictional vendor assignment. It is a prepared example, not an approved work order for a live matter:

{{read:workorder-example}}

Writing these instructions does not configure the application's permissions. A request not to send a message and a technical restriction that prevents sending are different protections. Implement and test the necessary controls in the authorized tool. The optional worksheet offers a place to draft the same assignment; the substantive questions are all above.
''')
add('agents',2,r'''
Watch for six recurring management failures. A **wrong objective** substitutes a convenient measure for the client's actual result. **Cascading error** turns an early mistake into the premise of later work. A **hidden omission** leaves out a source, issue, or affected person while producing complete-looking prose. **Permission creep** gives the agent more access or authority than the task requires. **Self-confirmation** treats another model response as independent support. **Silent uncertainty** turns a missing answer into a guess instead of returning it for a decision.

Each failure suggests a different intervention. Reviewing the objective will not find a missing amendment unless the source review also checks completeness. A stricter source requirement will not prevent an unauthorized email unless the system's action permissions address sending. Use the failure to select the control rather than demanding more caution in general.
''')
add('agents',4,r'''
Management continues after a successful test. Keep the records that the risk and assignment warrant, examine recurring failures, and update instructions when the law, sources, or system change. A workflow that repeatedly misses its standard may need a narrower job or retirement. This is part of managing the service, not a verdict on whether AI in general is useful.
''')

replace('writing',0,'Diagnose what the reader needs before requesting a rewrite.',r'''
“Make this clearer” leaves the most important writing choices unstated. Does the opening delay the answer? Does the sentence hide who acted? Does the analysis state a rule without connecting the facts to it? A useful revision begins with a diagnosis of the reader's problem.

That diagnosis also tells you which kind of assistance to seek. **Rewriting** can explore a heading, opening, or sentence whose emphasis and style deserve attention. **Editing** can identify confusing, cluttered, or dense passages without replacing them. **Drafting** can turn supplied substance into an email or other defined document when you understand the result well enough to judge it. A request to **summarize or organize** can make a collection of information easier to examine. **Analysis** can explore issues, themes, supporting arguments, and objections after your own first pass.

These tasks can recur throughout a matter. After gathering authorities, you might ask for several ways to organize their relevant propositions. After selecting a rule, you might ask which distinctions the proposed synthesis leaves unresolved. After writing, you might seek a diagnosis of where a reader needs another explanatory step. The workshop emphasizes small, useful contributions within the work rather than giving AI the whole task at once.

The examples below show how this looks in writing. Each includes the relevant passage and explanation. You can read the comparisons directly or try the separate exercise before returning; the teaching does not depend on submitting an answer.
''')
replace('writing',1,'A more specific request gives you a more useful comparison.',r'''
The fee-table example begins with a sentence that describes the table's intended purpose rather than what it does for the reader:

{{read:fee-original}}

The workshop then compares a general request for clarity, a request for a stronger verb, and more extensive guidance using examples and alternatives:

{{read:fee-options}}

The first response changes words but leaves the indirect construction largely intact. The second gives the sentence a more direct verb, yet no longer expressly distinguishes direct from indirect costs. The guided version uses “shows” while retaining that distinction. The important comparison is therefore not merely length or energy. It is what the reader understands and which meaning survives.

There are other defensible arrangements. The workshop's later options begin with the costs, frame the sentence as the investor's question, or split the explanation into two sentences. Those alternatives help you decide where to place the reader's attention. They are more informative than a set of synonyms that leaves the same sentence untouched.

Your own knowledge of sentence craft makes the request better. If you can identify a weak verb, an obscured actor, or an unnecessary description of intention, you can ask the system to address the problem and examine whether it did. A fluent response is not the same thing as a well-directed revision.
''')
replace('writing',2,"Teach a writing choice, not a writer's surface mannerisms.",r'''
The dog-toy introduction in the workshop demonstrates how a writer can give the reader something concrete to understand before introducing the legal dispute. The original practice passage begins abstractly:

{{read:dog-before}}

The workshop contrasts that passage with this excerpt from the opinion:

{{read:dog-after}}

The reader first encounters the subject and the company making it. The label changes then explain how the toy evokes the bottle. The concrete details do the explanatory work that phrases such as “design, marketing, and sale” or “commercial impression associated with it” leave to the reader.

A generic request for clarity may preserve the abstract opening and rearrange the same nouns. Better direction identifies what should change: name the actor, describe the product and conduct, give the reader the label comparisons, and let the legal issue emerge from those facts. A sample can demonstrate the move without supplying facts for a new matter.

The workshop's extended editing request follows a useful process. Diagnose the original and identify its core point. Develop meaningfully different candidates, evaluate them against stated criteria, select a small set worth examining, and explain which choices changed. A recommendation can then identify the best fit for the purpose. The explanation matters because it lets the writer learn and disagree; an unexplained score is not enough.

Preserve the ground rules from that example. Do not change an already effective passage merely to appear useful. Flag an ambiguity that requires a substantive decision instead of silently choosing. Keep source facts, quotations, and propositions intact. A brief, an opinion, and a client email may borrow an explanatory technique while requiring different tones. Copying a celebrated writer's fragments or distinctive metaphors is not the same thing as learning how that writer helps the reader.
''')
replace('writing',3,'Place an unresolved condition beside the decision it affects.',r'''
Stonebridge wants confirmation that it can pay a $12 million dividend. Here is the supplied passage:

{{read:stonebridge-original}}

The reported ratio is below the contractual ceiling only because it includes projected savings for which supporting material has not been provided. That relationship should be easy to see. A reader should not have to reconstruct it from the order in which the lawyer performed the review.

Here is a prepared revision from this guide, not an answer supplied in the original slides:

{{read:stonebridge-revision}}

The revision leads with what can be said now and connects the request for support to the deadline. The ratios then explain why the support matters. It preserves the three conditions for counting projected savings and the difference between “no separate default has been identified” and a finding that no default exists.

That is substantive editing as well as sentence editing. “The dividend is prohibited” would be more decisive and less faithful to the record. “Additional diligence is needed” would be shorter and less useful to the person who needs to provide the support. The writing should make the present uncertainty and its consequence precise.
''')
replace('writing',4,'Explain separate concerns as separate questions.',r'''
Falcon Medical's proposed disclosure raises a comparison between confidentiality obligations and a separate question about how much information the recipient needs. The original passage supplies both:

{{read:falcon-original}}

A signed NDA is not automatically an NDA that meets Section 9.12. The residuals clause may permit use that the credit agreement does not allow. The excess customer information creates a related concern, but reducing the package does not itself resolve the difference in contractual protections.

Here is the guide's prepared comparison:

{{read:falcon-revision}}

The first sentence gives the reader two questions to resolve rather than presenting signature of the NDA as the answer. The following paragraphs explain the legal comparison and the unnecessary detail in the package. The conclusion remains conditional: the NDA may be less protective.

The original passage suggests revising the NDA or removing information. This guide adds the caution that narrowing the package should not be treated as a complete legal cure without examining what would remain and what the agreement permits. That caution is an explanatory addition; the source does not supply a final legal determination. Separating the concerns makes the further analysis visible instead of using a cleaner sentence to hide it.
''')
add('writing',5,r'''
Sometimes identification is the better assignment. Ask the tool to locate every sentence where a reader must hold several ideas at once, every transition that leaves the relationship unexplained, or each place the application of a rule is asserted rather than developed. Ask it to point to the words and explain the problem. You can decide what to revise before the draft is changed.

Other times you need help with tone or technical explanation. Supply the accurate substance and describe what the reader knows. Ask for ways to introduce the unfamiliar idea through a concrete example, while marking any new analogy as an illustration rather than source evidence. The result still has to preserve the distinction or condition the legal analysis depends on.
''')

replace('aiisms',2,'A plain paragraph can still have no useful analysis.',r'''
The workshop uses this deliberately weak paragraph to show why the edit must reach beyond words:

{{read:aiism-passage}}

At the word level, phrases such as “crucial to underscore” and “multifaceted challenge” announce importance without explaining it. At the sentence level, the repeated transitions and the “not merely” contrast supply a rhythm instead of a developed relationship among the ideas. The hedges describe uncertainty without identifying what remains unresolved.

The larger problem is substantive. The paragraph does not identify the controlling authority, connect a particular fact to a legal requirement, rank the competing concerns, or propose a next action the client can use. Removing the conspicuous language would leave those omissions untouched. A recommendation to “carefully consider its options” offers no basis for choosing among them.

The appropriate edit therefore depends on the available sources. The paragraph's label for the conduct may itself go beyond the record. Before drafting a more definite recommendation, identify what the law requires, what the evidence establishes, and what the client needs to decide. Where those materials are absent, say what must be obtained rather than inventing a more concrete answer.

Some of the workshop's contrast passages make this point from the other direction. Ordinary legal writing can contain a contrast, a long sentence, or the word “moreover” and still perform useful analytical work. A plain-sounding recommendation can remain generic because it never applies the rule or weighs the facts. The habits are prompts for inspection, not proof of authorship or automatic reasons to delete a sentence.
''')
add('aiisms',0,r'''
The source describes two complementary approaches: give clearer directions before drafting, and learn to recognize the patterns during editing. A drafting request might ask the system to introduce the answer promptly, vary sentence and paragraph length according to the material, avoid inflated business language, and develop the relationship among ideas. It should not replace one compulsory rhythm with another.
''')
add('aiisms',4,r'''
A useful style description also distinguishes your habits from your team's requirements. The workshop asks about full-sentence headings, paragraph length, where the answer appears, contractions, first-person usage, numbered points, and what the first sentence normally does. For a group, the relevant choices may include memo format, defined terms, citation placement, phrases reviewers regularly remove, or vocabulary the group avoids.

Use approved samples to describe those decisions, then challenge an answer that merely flatters. Push until it says something specific enough to correct. Save the reviewed description with the examples and adapt it to the audience. The numerical “voice vector” and fixed rhythm in one slide are illustrative prompt variables, not required rules for this guide or a universal account of my voice. Here, the material should govern the rhythm, and complete explanations matter more than matching a sentence-length target.
''')

replace('process',1,'Examine each part of the service before choosing the technology.',r'''
I use nine stages to examine a proposed process improvement. They begin with the client and end with a tested revision, so the choice of a product follows an understanding of the service.

### Define the outcome and map the current work.

State the change that should happen for the client: a decision made, a dispute resolved, a right exercised, a risk reduced, or a burden removed. Then describe how the service currently reaches that result. Include the client, staff, lawyers, courts, vendors, and systems where they play a role. Show the inputs, handoffs, waiting, decisions, and repeated work, not only the legal drafting steps.

### Find friction and failure, then remove before adding.

Look for duplicated requests, unclear responsibility, information gaps, inconsistent judgment, and places where errors remain hidden. Ask whether each step protects something valuable. Remove a step that contributes nothing; standardize work that ought to be consistent. A simpler instruction or clearer assignment may solve the problem before AI becomes necessary.

### Assign the best actor and build the controls.

Decide which work belongs to the client, a lawyer, a staff member, an AI tool, an agent, or an outside expert. Pair the assignment with the source requirements, permissions, approvals, and stopping conditions that address its risk. This includes deciding where a lawyer must weigh competing values rather than merely complete a checklist.

### Pilot narrowly and measure the whole result.

Test a limited use with representative users and examples near the boundaries. Observe quality, time, cost, correction work, client effort, accessibility, equity, and learning. A faster first draft is not enough evidence if the reviewer needs more time to repair it or the client needs more help to understand it.

### Revise and version.

Examine what happened, record the change, and test again. The source treats failure and feedback as information for the next version. A process that cannot meet its standard should not continue merely because the team has invested effort in it.

These paragraphs follow the source's nine stages: define, map, find, remove, assign, control, pilot, measure, and revise. They are an investigation of the service, not a claim that filling out nine fields proves the redesign works.
''')
replace('process',2,'A process map can reveal a problem another memo would miss.',r'''
Consider a fictional intake process. The client enters information in a form, an assistant retypes it into a summary, a lawyer asks follow-up questions, and the client supplies information that could have been requested at the outset. Drafting the summary faster addresses only one step. It does not resolve the duplicate entry or the unclear question that caused the follow-up.

A useful map identifies the people involved, what each needs from the preceding step, and where a decision must be made. Perhaps the assistant should receive structured information directly. Perhaps a plain-language explanation belongs beside a confusing question. Perhaps a lawyer needs to speak with the client before the remaining form can sensibly be completed. Those are different improvements, and only some may benefit from AI.

Several further questions help examine the proposed service. Who is trying to accomplish what, and where does the current service impose confusion, effort, delay, or exclusion? What should change in the world? Which steps protect value and which persist by tradition? Where must a lawyer weigh uncertainty and consequences? What control protects each risky step? How will failures, feedback, and changed law improve the next version?

The map is an analytical tool, not proof that the service is safe or useful. It gives the people responsible for the work something concrete to question. The optional process worksheet records the same inquiry for a service you bring.
''')
add('process',3,r'''
NIST's framework uses the terms **govern**, **map**, **measure**, and **manage**. The source applies them as an organizational perspective: identify ownership, understand the context and affected people, examine performance and risk, and decide how to respond and improve. That larger perspective helps connect an individual workflow with responsibility for the service as a whole.
''')

replace('building',2,'Six questions separate a prototype from a responsible pilot.',r'''
A prototype shows that an idea can be explored. It does not establish that the tool is accurate, secure, maintained, legally compliant, or ready for public use. Before someone depends on the tool, the team should be able to explain six areas of the proposed use.

**User validation** asks whether representative users have tried the tool and what the team observed. Confusion, workarounds, inaccessible features, and unexpected needs are evidence about the design. A successful demonstration by its creator answers a different question.

**Legal logic and sources** asks whether the relevant rules are current, jurisdiction-specific, traceable, and within the proposed scope. The tool should distinguish authority from inference and general information from advice. A legal rule may also include exceptions or judgment that cannot responsibly be hidden behind a yes-or-no result.

**Failure behavior** asks what happens with missing facts, conflicting sources, ambiguity, instructions trying to redirect the system, and requests outside scope. A test should state the expected behavior before it runs. Sometimes the correct result is to stop and ask a lawyer.

**Data and security** concerns the authorized environment and the permissions, retention, logging, access, and inputs the task actually needs. A working interface does not answer these questions. The relevant technical and organizational review still has to occur.

**The human path** asks whether users can reach an accountable person and whether that person handles consequential decisions, exceptions, individualized judgment, and external actions. A disclaimer is not a substitute for the route to help that the service requires.

**Ownership and maintenance** asks who watches performance, updates sources, approves changes, rolls back a bad version, and retires the system. The service needs that responsibility after launch as well as before it.

The optional review worksheet records the evidence behind these questions. Its checkmarks do not verify the evidence or certify readiness. The standard is the team's ability to explain the use and demonstrate the relevant behavior.
''')
add('building',1,r'''
The source places the lawyer's contribution in problem selection, requirements, legal logic, test design, user experience, and governance. That is a practical way to collaborate with a technical specialist: bring a recurring problem worth solving, explain the rule and exceptions, identify the consequences of failure, and describe behavior you can test. The collaboration gives your legal knowledge a more direct role in building the service.
''')

replace('playbook',1,'Record enough for another lawyer to understand the method.',r'''
A useful playbook has six parts, each serving a different purpose. **Principles** explain what AI should help expand and which judgments you intend to protect. **When-not-to-use rules** identify uses that are prohibited, unsafe, harmful to learning, or more expensive to verify than to do yourself. A **prompt and harness library** keeps reusable instructions with the source requirements and examples behind them.

**Workflow and process** shows where assistance belongs in the assignment and where human decisions occur. **Failures** records hallucination, omission, overbreadth, bias, narrowed thinking, or implementation problems and examines why they happened. A **personal development plan** identifies the legal and managerial skills you will practice independently, with AI assistance, and as a supervisor of AI-enabled work.

A useful entry is specific enough to apply and limited enough not to invite careless reuse. Here is a prepared example:

> **Method:** Compare alternative openings for an advice paragraph after determining what the record supports.  
> **What helped:** Asking one version to foreground the unresolved condition and another to foreground the information the client needs to supply made the choice of emphasis visible.  
> **What I rejected:** An opening that converted “cannot yet confirm” into “prohibited.”  
> **What must travel with the prompt:** The accurate rule, facts, intended audience, and material qualifications.  
> **Limit:** This improves the explanation; it does not establish that the underlying advice is correct.

Someone reading that entry can understand why the method helped and where the lawyer still had to make a decision. Saving only the successful-looking paragraph would lose that lesson. The optional playbook form provides a place to record entries of your own.
''')

replace('leadership',1,"Keep the profession's unresolved questions in view.",r'''
What should legal work look like when producing answers becomes easier? We do not have final answers. Keeping those questions visible is part of the guidance rather than an assessment to complete.

Consider what deserves a law license and what has been reserved to lawyers mainly by tradition. Consider which tasks exist because information used to be scarce and which forms of judgment remain important even when information is abundant. Those questions affect the design of services, regulation, and the opportunities a lawyer should investigate.

The client questions are equally important. What should remain human because it involves trust, empathy, legitimacy, or the meaning of a person's life? How should fees reflect judgment, risk, availability, and access when production time falls? Who should receive the gains in time or cost, and who bears an error produced across several people and systems?

There are also questions about institutions. How does advocacy change when AI may summarize or mediate the work before a person reads it? How will novices develop expertise when traditional training tasks are automated? Can technology improve access without scaling poor advice? How should lawyers lead teams that include clients, staff, experts, agents, and platforms?

The [questions for the profession](#/questions) collect the source guides' broader inquiry by subject, including clients, public access, legal institutions, and law's role in an AI society. They are readable without selecting a question or writing a response. The optional reflection worksheet is there for readers who want to record how experience changes their views.
''')
add('leadership',0,r'''
We should also ask what previously uneconomic solution could now exist. That question directs attention beyond the matters already arriving at a firm's door. Preventive services, small claims, and problems facing underserved communities may call for a different delivery model rather than a cheaper version of the same document. The possibility needs testing, boundaries, and a human path where required, but it belongs beside the discussion of risk.

The broader questions about AI as an audience should remain questions rather than a recipe for manipulating a system. Can the legal point survive a summary? Does the writing connect the source with the proposition clearly enough for a human reviewer to inspect? How do we preserve nuance and minority views when several people use similar tools? The source invites lawyers to examine that changing environment without flattening the argument or trying to game the reader.
''')
add('leadership',2,r'''
A mixed team needs more than instructions for the model. Clarify who is responsible for each handoff, who may challenge a conclusion, and who has the authority and time to investigate. Protect the ability to disagree even when the proposed answer appears unanimous because several systems produced similar prose. Agreement among tools does not remove the need for sources or accountable judgment.
''')
replace('leadership',3,'Judge progress by capabilities you can demonstrate.',r'''
We can judge our progress through eight capabilities. You can **frame before prompting**, forming an initial map or theory and using AI to widen it. You can **classify risk**, distinguishing harm to others from harm to your own reasoning and choosing controls for the actual problem. You can **verify**, connecting authority, facts, reasoning, client fit, and process compliance with appropriate evidence.

You can **manage agents** by specifying the work, allocating authority, setting feedback points, testing behavior, and returning uncertainty to a person. You can **improve a process** by mapping the service, removing waste, assigning work well, measuring the result, and revising it. You can **build and test** by translating a legal problem into requirements, exploring a prototype, identifying its limits, and governing deployment.

You can **lead** by protecting candor, accountability, client value, and the public interest while the work changes. And you can **own the result** by explaining what the technology did, what you did, what you rejected, and why the final judgment is yours.

These capabilities connect the whole guide. Knowing a product's newest feature is not the same as demonstrating them. Nor does checking every exercise establish them. The evidence is in your ability to direct the work, explain its basis, and improve the service someone actually receives.
''')
