/* Write.law guide-first edition: complete reading and source-grounded references. */
const SOURCES = [
  {
    "id": "fall",
    "short": "AI-enabled lawyering",
    "title": "The AI-Enabled Lawyer",
    "file": "Regalia AI Guide 2026 Fall.pdf",
    "pages": 18,
    "description": "Joe Regalia’s teaching framework for professional judgment, responsible use, workflows, building, and leadership. The public edition adapts the course framing for lawyers and law students.",
    "note": "Joe Regalia’s teaching framework for professional judgment, responsible use, workflows, building, and leadership. The public edition adapts the course framing for lawyers and law students."
  },
  {
    "id": "student",
    "short": "AI foundations",
    "title": "AI for Law Students",
    "file": "AI For Law Students Regalia1 (1).pdf",
    "pages": 22,
    "description": "Joe Regalia’s introductory teaching material. The public edition explains stable concepts without treating historical product names, statistics, or descriptions as current guarantees.",
    "note": "Joe Regalia’s introductory teaching material. The public edition explains stable concepts without treating historical product names, statistics, or descriptions as current guarantees."
  },
  {
    "id": "short",
    "short": "Responsible-use checklist",
    "title": "Using AI This Semester: A Short Guide",
    "file": "AI Two pager.pdf",
    "pages": 2,
    "description": "The before, during, and after checklist, four-minute self-assessment, and use-note pattern are adapted for professional and educational assignments.",
    "note": "The before, during, and after checklist, four-minute self-assessment, and use-note pattern are adapted for professional and educational assignments."
  },
  {
    "id": "slides",
    "short": "Writing and prompting",
    "title": "Leveling Up Your AI Prompting",
    "file": "Beautiful.ai - AI Skills and AIisms(2).pdf",
    "pages": 87,
    "description": "Joe Regalia’s workshop materials supply the collaboration practices and writing exercises. Original exercise passages retain their substantive facts. Client-branded slide images are not distributed in this guide.",
    "note": "Joe Regalia’s workshop materials supply the collaboration practices and writing exercises. Original exercise passages retain their substantive facts. Client-branded slide images are not distributed in this guide."
  },
  {
    "id": "graph",
    "short": "Workflow teaching module",
    "title": "Mapping an AI-assisted workflow",
    "file": "The preceding guide in this conversation",
    "pages": null,
    "description": "The fictional vendor assignment was developed for this guide. It illustrates work planning and review; it does not decide an actual termination dispute.",
    "note": "The fictional vendor assignment was developed for this guide. It illustrates work planning and review; it does not decide an actual termination dispute."
  }
];
const PARTS = [
  {
    "name": "Foundations",
    "tag": "Decide where AI belongs in your work.",
    "desc": "How lawyers add value, how the tools work, and how to protect independent judgment while choosing a responsible use.",
    "title": "Decide where AI belongs in your work."
  },
  {
    "name": "Systems",
    "tag": "Make the work easier to direct and review.",
    "desc": "The working methods for prompting, legal writing, source management, workflows, and supervision of AI agents.",
    "title": "Make the work easier to direct and review."
  },
  {
    "name": "Building",
    "tag": "Improve a service and test a proposed tool.",
    "desc": "How legal insight can improve a service and become a useful tool, with testing before anyone depends on it.",
    "title": "Improve a service and test a proposed tool."
  },
  {
    "name": "Leadership",
    "tag": "Carry what you learn into your practice.",
    "desc": "How to preserve what we learn, develop people, and decide what AI should change about the profession.",
    "title": "Carry what you learn into your practice."
  }
];
const CHAPTERS = [
  {
    "id": "lawyer",
    "part": 0,
    "title": "Good AI work begins with good lawyering",
    "nav": "Your role as a lawyer",
    "desc": "AI gives us more ways to work with legal knowledge. Our contribution is deciding what deserves attention, how the assistance should be used, and what will help the person behind the problem.",
    "sources": [
      [
        "fall",
        "pp. 1–3, 18"
      ],
      [
        "student",
        "pp. 1–2"
      ]
    ],
    "sections": [
      {
        "h": "AI changes what we can do with legal knowledge.",
        "html": "<p>Law is made of language. We read it to find out what happened, work through what the rules require, and explain what someone should do. For a long time, our technology helped us find and move the words. Now it can help produce them, including the analysis and argument those words contain.</p>\n<p>That gives lawyers much more to consider than how quickly we can finish a first draft. We can explore an argument we would otherwise have set aside for lack of time. We can ask a patient tutor to explain unfamiliar technical material, compare several ways of presenting an issue, or build a small tool around a recurring client problem. My interest in AI begins with that wider opportunity: what could we do better, or do for the first time, if the work were easier to explore?</p>\n<p>But everyone can ask a system to produce an answer. A lawyer's contribution has to extend beyond the request. We need to understand the problem well enough to decide whether the answer helps, which questions it misses, and what the person receiving it can reasonably do with it. Our writing and analytical skills therefore remain part of the method, even when a tool performs more of the production.</p>\n<p>This guide brings those questions together. Foundations concerns our role, independent judgment, and responsible use. Systems develops the skills and processes for working with AI. Building examines how legal insight can become a better service or a tool. Leadership asks how we should manage the work and shape the profession as those possibilities change. You can read the chapters in order or return to a particular subject when your work calls for it. The explanations stand on their own; exercises and worksheets are optional companions.</p>\n<p>Consider a client who asks whether it can terminate a software contract. Before asking AI to analyze the agreement, find out why the client wants out. Repeated outages may be interrupting its business. It may have found a cheaper alternative. Or it may prefer to keep the vendor if the relationship can be repaired. Those are different problems, even when they begin with the same legal question.</p>\n"
      },
      {
        "h": "The lawyer turns uncertainty into a decision someone can use.",
        "html": "<p>I describe the lawyer's job as converting legal uncertainty into responsible action for people and institutions. That description includes the answer, but it also includes the work that makes the answer worth acting on.</p>\n<p>We <strong>frame</strong> the problem by distinguishing the client's objective from the question first presented to us. We <strong>judge</strong> among imperfect options, weighing the law alongside timing, cost, relationships, and consequences. We <strong>design</strong> how the work will get done so that a useful analysis can become a dependable service. Those responsibilities may send us back to the beginning of an assignment. Learning that the client cannot tolerate a service interruption, for example, changes what deserves attention in the termination analysis.</p>\n<p>We also <strong>counsel</strong> the person behind the facts. A recommendation can be legally available and still wrong for someone who cannot bear its practical consequences. We <strong>challenge</strong> the emerging answer by examining assumptions, adverse support, and objections that deserve a hearing. Finally, we <strong>own</strong> the work we approve. We should be able to explain what was sent, filed, advised, or built, including the uncertainty that remains.</p>\n<p>These are not six jobs performed in a fixed order. They overlap within a matter. You may counsel the client, discover a different objective, revise the research assignment, and then reconsider an earlier recommendation. AI can help you investigate each question, but a well-written response does not tell you that you asked the right question in the first place.</p>\n"
      },
      {
        "h": "Supervising AI draws on skills lawyers already use.",
        "html": "<p>You do not need to become a software engineer to start working this way. Think about a well-run assignment to a junior lawyer. You explain the question, supply background they would not otherwise know, and describe what you need back. For a difficult matter, you may ask to discuss the research before they draft. You also make clear which decisions require your involvement.</p>\n<p>Much of that discipline carries over to AI. The difference is that you should not assume the system shares a colleague's understanding of the matter or will recognize when an instruction needs clarification. Make important limits explicit, and check what the tool actually did. Later chapters show how to organize those instructions, sources, and reviews into a repeatable process.</p>\n<p>These skills matter at every career stage. A student can practice by planning a fictional assignment and explaining where review belongs. An experienced lawyer can apply the same questions to a recurring matter that the team already understands. In both settings, the aim is to make the work easier to direct and evaluate.</p>\n\n<p>The expanded role also includes project management: sequencing work, allocating responsibility, and keeping deadlines, budgets, and dependencies visible. A team needs to know which finding the next task depends on and who can resolve a question when the source is incomplete. As an AI-agent manager, you make the same decisions about a system that may take several steps before returning to you.</p>\n<p>A lawyer can also become a builder without first becoming a software engineer. Legal knowledge helps identify the problem, translate a rule and its exceptions into requirements, and devise tests that expose a bad answer. Working with technical experts remains important where the proposed use calls for expertise you do not have. The contribution is knowing what the tool should accomplish and what evidence would establish that it does.</p>\n<p>Leadership connects these roles. Someone decides whether a faster process will mean more time to counsel clients, lower costs, better service, or only a higher volume of output. Someone also needs to protect junior lawyers' development when the tasks that once taught a skill are shortened or automated. Those decisions belong in our discussion of AI, not outside it.</p>\n"
      },
      {
        "h": "Choose an AI contribution you can judge.",
        "html": "<p>Start with a task you understand well enough to assess. After reading two contract provisions, you might ask AI to identify their differences. After developing an argument, you might ask what a skeptical reader would need explained. Each request gives the system a useful job without handing it every decision in the matter.</p>\n<p>Before you send the request, decide what would make the response useful. A comparison should preserve differences that affect meaning and point you to the language behind them. A critique should engage with your reasoning, rather than recite objections that could apply to any argument. This gives you a standard beyond whether the answer sounds polished.</p>\n<p>Your initial view may change. That is often the benefit of using another perspective. What matters is that you can explain the change. If the system identifies an exception you missed, return to the source and decide what the exception does to your analysis.</p>\n"
      },
      {
        "h": "Look beyond making the existing task faster.",
        "html": "<p>My workshop materials describe three broad opportunities. The first is improving work you already do. A lawyer can use AI to examine a heading, develop another way to explain an exception, or find the places where a paragraph skips part of the analysis. The task remains recognizable, but you have more ways to improve it.</p>\n<p>The second is making a useful process repeatable. An editing checklist can become a sequence that identifies potential issues, preserves their locations, and brings them back for a lawyer's review. A source collection, annotated examples, and recorded decisions can make the next assignment easier to begin. The time saved is only part of the benefit. A repeatable process can also make previously invisible decisions easier to inspect.</p>\n<p>The third is attempting work you previously could not justify. You might explore several theories before choosing which deserve investigation, study a set of public opinions for recurring approaches to a question, or prototype a service for clients whom a traditional delivery model does not reach. These are possibilities to investigate, not assurances about what a particular model will do. A pattern in a judge's opinions, for example, is material for analysis; it cannot establish how that judge will decide the next case.</p>\n<p>Across all three, the important unit is often a contribution within the larger task. You can seek alternatives while researching, feedback while outlining, and a specific comparison while editing. You do not have to hand over the whole matter to get substantial value from assistance. The following chapters develop the judgment needed to choose those contributions and use them well.</p>\n"
      }
    ],
    "quiz": {
      "q": "After receiving a convincing recommendation, what should the lawyer establish before relying on it?",
      "a": [
        "Whether a shorter version would be easier for the client to read.",
        "Whether the recommendation is supported and fits the client’s actual circumstances.",
        "Whether the tool can produce the same recommendation in another style."
      ],
      "correct": 1,
      "why": "Readability may matter, but it does not establish that the recommendation is sound. The lawyer needs to examine its basis and suitability for the client."
    },
    "references": []
  },
  {
    "id": "basics",
    "part": 0,
    "title": "Understand the tool well enough to direct it.",
    "nav": "How the tools work",
    "desc": "You do not need an engineering background to use AI thoughtfully. You do need to distinguish what the model generates from what it retrieves, and a written instruction from a control the software actually enforces.",
    "sources": [
      [
        "student",
        "pp. 2–10, 19–22"
      ]
    ],
    "sections": [
      {
        "h": "A generated answer is different from a source you have checked.",
        "html": "<p>Artificial intelligence covers a broad range of systems. Some classify information or predict an outcome. Others generate content. This guide focuses on the language tools lawyers use to work with documents and ideas, which are built around large language models.</p>\n<p>A language model learns patterns during training and uses them to generate a response. An application may also provide your documents, retrieve material from a database, or let the model use another tool. When you ask a legal question, the answer might therefore draw on several different kinds of information. Find out which ones were available for the particular response you are reviewing.</p>\n<p>Suppose a tool gives you a case citation and a paragraph explaining its holding. The citation's appearance tells you little about whether the case exists or supports the proposition. Even when the case is real, the explanation might confuse the court's holding with a party's argument. The term <strong>hallucination</strong> is commonly used for false or invented content, but smaller distortions deserve the same attention. A summary that changes “the plaintiff alleges” to “the defendant did” has changed the facts you are being asked to rely on.</p>\n<p>The practical habit is to connect important statements with their supporting material. Then read that material in context. Asking the tool to include citations makes this review easier; it does not perform the review for you.</p>\n\n<p>It also helps to distinguish training from use. During training, the model's parameters are adjusted as it learns patterns from data. When the model responds to a request, it is running with those learned parameters; this is called inference in AI engineering. A response may also use material supplied at that moment. Providing an opinion for an assignment is therefore different from training the model on that opinion.</p>\n<p>Describing the foundation as prediction does not capture everything a finished product can do. A system may have additional training and tools that let it work through several tasks, retrieve material, and check intermediate results. Evaluate that finished system. Neither calling it “autocomplete” nor calling it “reasoning AI” tells you whether it can perform the particular legal work you have in mind.</p>\n"
      },
      {
        "h": "The model and the application have different jobs.",
        "html": "<p>The model is one part of the product you use. The surrounding software determines what files it can read, whether it can search, and which actions it may take. Developers sometimes call that surrounding system a <strong>harness</strong>. Think of the model as an engine and the application as the rest of the car: the engine matters, but so do the controls and where the car can go.</p>\n<p>Two products using the same underlying model may handle your work quite differently. One may search an approved collection of legal materials. Another may let you upload a contract but have no access to the amendment stored elsewhere. One may draft an email for review; another may have permission to send it.</p>\n<p>When someone demonstrates a product, ask to see those details. Which documents supported the answer? What happens when a file cannot be read? Can the system send something before you approve it? Understanding the application gives you a better basis for evaluating the proposed use than the model's name alone.</p>\n"
      },
      {
        "h": "Keep an accurate record outside the conversation.",
        "html": "<p>The <strong>context window</strong> is the information a model can consider while generating a response. Its capacity is measured in <strong>tokens</strong>, small units of text or other encoded input. A long conversation may be shortened or summarized to fit the available space. Product memory features work differently and should not be treated as a dependable record of every instruction or decision.</p>\n<p>For a continuing matter, keep the current assignment and reviewed findings in a separate reference document. Imagine returning to a contract analysis after a new amendment arrives. The next session needs to know that the amendment now controls, which earlier conclusions require reconsideration, and which questions remain open. “Continue where we left off” may not supply any of that.</p>\n<p>You can ask AI to prepare the reference document, but review it before using it again. Mark the difference between a suggestion the system made and a decision you approved. Otherwise, the saved summary can turn an unaccepted proposal into the starting assumption for the next session.</p>\n<p>Context capacity is also separate from confidentiality. What a model can consider in a response does not tell you how long the provider retains your files or who can access them. Those questions require checking the actual service, account settings, and applicable terms.</p>\n"
      },
      {
        "h": "A few distinctions explain most of the vocabulary.",
        "html": "<p><strong>Retrieval-augmented generation</strong>, often called <strong>RAG</strong>, combines finding material with generating an answer from it. A research product might retrieve cases; a document tool might find provisions in your agreements. Finding relevant material and interpreting it are separate jobs. A useful result needs both. The source collection also matters: a beautifully written account of the wrong documents does not answer the assignment.</p>\n<p>A <strong>reasoning model</strong> is designed to devote additional computation to working through a problem. That can be useful for a multi-step question, but the product label is not a substitute for examining its answer. A displayed reasoning summary is something to review, not evidence that the reasoning or result is correct.</p>\n<p>An <strong>agent</strong> can pursue a task through several actions. It might search, read what it found, prepare a comparison, and decide which action to take next. This shifts some of your attention from a single response to the chain of work. You need to know what information and authority the system has and which decisions must return to a person.</p>\n<p>An <strong>API</strong> lets software communicate with another system. A <strong>multimodal</strong> product works with more than one kind of material, such as text and images. <strong>Open weights</strong> refers to published model parameters that can be run elsewhere, subject to the applicable terms. <strong>Fine-tuning</strong> adds training to an existing model. These features answer different questions. None, on its own, establishes that a product protects information or is suitable for a client matter.</p>\n<p>The <a href=\"#/glossary\">glossary</a> provides a fuller reference, including terms used in the original introductory guide. You do not need to memorize them. Use the distinction when it helps you ask a better question about the system in front of you.</p>\n"
      },
      {
        "h": "Test the use you are considering.",
        "html": "<p>A system can perform well on one task and poorly on a nearby one. A clear summary of a provision does not establish that it will find every exception across a collection of agreements. Nor does a successful demonstration establish how it handles an unreadable page or a missing document.</p>\n<p>Start with material you understand and a result you can check. For a clause-comparison task, identify an important difference yourself, then see whether the system finds and explains it. Change the example so a necessary provision is missing. Does the response report the gap, or continue as though the documents were complete?</p>\n<p>These small tests give you more useful information than asking the system whether it is good at legal analysis. Keep a record of what worked, what failed, and what you changed. You will return to that habit when we build more substantial workflows.</p>\n\n<p>There are two other reasons to test the actual task. First, responses can vary. That variability is useful when exploring alternatives and troublesome when you need consistent extraction. Second, capability can be uneven: a system may produce sophisticated prose yet mishandle a date or overlook a small qualification. Success on the harder-looking task does not establish competence on the easier-looking one.</p>\n<p>Product categories are a more useful starting reference than an old list of version numbers. General assistants support conversation and broad drafting. Search and study tools organize answers around retrieved or supplied material. Legal research products add legal sources and research features. Practice platforms coordinate document work and workflows. Writing and citation products focus more narrowly on editing or connecting claims with support. A product may span several categories, so inspect what the relevant feature actually does. Historical product examples from the original guide are identified as such in the source notes rather than presented as a current buying guide.</p>\n"
      }
    ],
    "quiz": {
      "q": "An AI application cites an uploaded document. What does that tell you?",
      "a": [
        "The source check is complete because the answer includes a citation.",
        "Uploading the document means that every relevant passage was considered.",
        "The citation identifies material you should inspect; it does not establish that the document was fully or accurately interpreted."
      ],
      "correct": 2,
      "why": "The cited passage may be useful evidence, but you still need to compare the claim with the source and consider whether important material is missing."
    },
    "references": [
      {
        "title": "Anthropic: Effective context engineering for AI agents",
        "url": "https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents"
      }
    ]
  },
  {
    "id": "permission",
    "part": 0,
    "title": "Decide whether AI belongs in this assignment.",
    "nav": "When to use AI",
    "desc": "Before you open a tool, identify the use you are considering and what would make it appropriate. Permission, information handling, and your ability to check the result can change from one task to the next.",
    "sources": [
      [
        "fall",
        "pp. 5–7"
      ],
      [
        "short",
        "pp. 1–2"
      ],
      [
        "slides",
        "pp. 4–6"
      ]
    ],
    "sections": [
      {
        "h": "Ask about a particular use, not AI in general.",
        "html": "<p>“Are we allowed to use AI?” is usually too broad a question. A firm might approve a tool for public research without approving it for confidential deal documents. A client agreement may impose limits beyond the firm's general policy. In a course, feedback on your draft might be permitted even when an AI-generated first draft is not.</p>\n<p>Describe the proposed use before deciding whether to proceed. For example: “I want this approved application to compare the termination provisions in these two agreements and return a table for my review.” You can then ask whether the applicable rules permit that task with those materials in that system.</p>\n<p>I use five questions to organize the decision. Is the use allowed? Is the information appropriate for the system? What could happen if the answer is wrong? How would I verify it? And how much of the work should I do first? A useful answer names the policy, source, reviewer, or preliminary work involved. “I will be careful” leaves all of those decisions open.</p>\n"
      },
      {
        "h": "Answer the five questions for the particular use.",
        "html": "<p><strong>Is the use allowed?</strong> Identify the assignment, workplace policy, court requirements, client agreement, platform terms, and applicable law that bear on the proposed task. Permission to use a product is not permission for every action or every category of information. In a course, the purpose of the assignment can impose a further limit even when the tool is available.</p>\n<p><strong>Is the input safe?</strong> Determine what information the task needs and whether the system is approved to receive it. Privileged, confidential, personal, sealed, and proprietary information should not be treated as interchangeable with a public opinion. Removing a name does not necessarily make a document appropriate to share. The answer needs to address the actual material and the authorized setting.</p>\n<p><strong>What happens if the output is wrong?</strong> Consider who would rely on it and what could follow. An error might distort a record, cause delay, disclose information, or contribute to a decision that is difficult to reverse. The possibility of correcting a draft before it leaves the office is different from discovering the same error after the client has acted.</p>\n<p><strong>Can I verify it?</strong> Name the source, record, test, or reviewer that will establish whether the important parts are reliable. “Someone will look at it” is not yet a review plan. If the task is beyond your ability to evaluate, narrow it or identify the necessary expertise before relying on the result.</p>\n<p><strong>Should I do the first pass?</strong> Ask what understanding you need to bring to the task and which skills the task is meant to develop. Reading the case, synthesizing the rule, and choosing priorities may be the work you most need to do before asking for help. The next chapter explains how the first pass can vary with the assignment.</p>\n<p>The source guide groups uses into green, yellow, and red as a starting way to think about control. Green covers relatively low-stakes assistance you can evaluate, such as formatting or tone options after your own review. Yellow includes summaries, clause alternatives, and analysis that may influence formal work; these need active direction and substantive checks. Red includes restricted data in public tools, unverified law or facts in formal work, and unsupervised individualized advice. The source treats those uses as inappropriate unless authorized and highly controlled and verified. The colors do not approve the use. A supposedly minor edit can still alter meaning or expose information.</p>\n"
      },
      {
        "h": "Consider what AI may do to your thinking, too.",
        "html": "<p>Some risks are easy to describe: an incorrect citation, a missed exception, or information sent somewhere it should not go. Other risks arise earlier, while you are deciding what the problem is. A plausible first answer can draw your attention toward one theory and away from another before you have examined the facts yourself.</p>\n<p>Think about a lawyer who asks AI to rank the strongest arguments before reading the record. Nothing has been filed, and no client has yet relied on the answer. Still, the lawyer may begin the research inside a frame the system supplied. A later source check will not necessarily reveal the question that never made it onto the list.</p>\n<p>That is why I distinguish risk to the work from risk to our thinking. Both matter in practice, and the second also matters when the purpose of an assignment is to develop a skill. Before asking for options, form an initial view of your own. After considering the response, return to the problem and ask what both of you might have missed. This is a working habit to test and refine, not a guarantee against bias.</p>\n\n<p>The distinction produces four different situations. Brainstorming can have little immediate external consequence but substantial thinking risk: an early menu can determine which questions you investigate. A first human list, AI expansion, and another human pass address that problem more directly than checking the eventual citations alone.</p>\n<p>AI-first strategy or dispositive drafting can combine high thinking risk with high external risk. The source recommends avoiding those uses unless the work is highly controlled, grounded in a human first pass, and directed toward alternatives and challenges. At the other end, a non-substantive format change usually calls for engagement with the edited result rather than an elaborate strategy review.</p>\n<p>Citation, quotation, and record-location checks may be less likely to choose your theory for you, yet errors in those tasks can have serious external consequences. They require a dependable checking process and human verification. These examples explain why “low risk” is incomplete unless we say which risk we are discussing.</p>\n"
      },
      {
        "h": "Stop at a concern you cannot resolve.",
        "html": "<p>Suppose an AI summary attributes a statement to an attachment you cannot open. You can describe the issue precisely: “This conclusion depends on the missing attachment, so I cannot verify it yet.” That tells the next reviewer what is needed. Calling the answer “probably right” does not resolve the gap.</p>\n<p>The same approach applies when a system requests broader access than its assignment needs, or when you are uncertain whether particular information may be shared. Pause the affected work and identify who can answer the question. You may be able to continue with an authorized part of the assignment, but do not let that progress conceal the unresolved issue.</p>\n<p>For students, the relevant person may be an instructor or clinic supervisor. In practice, it may be the matter lead, the person responsible for information security, or the client through the appropriate communication. The useful habit is the same: state what you do not know, why it matters, and what would let the work proceed responsibly.</p>\n\n<p>The short guide identifies specific reasons to stop and ask: conflicting instructions, access beyond what the task requires, sensitive inputs, a material source that cannot be located or validated, a consequential use such as advice or filing, an unexplained material conclusion, or certainty that the facts and law do not support. A stop does not have to abandon the matter. It can return a focused question, identify the missing source, or restrict the next step to work that is authorized and checkable.</p>\n"
      }
    ],
    "quiz": {
      "q": "You cannot identify how to verify an answer that may affect a client. What should you do?",
      "a": [
        "Proceed after asking the AI to describe its confidence.",
        "Pause and establish an appropriate source or review process before relying on the result.",
        "Use a second model and proceed if the two answers agree."
      ],
      "correct": 1,
      "why": "A confidence statement or another generated answer does not resolve the missing check. Identify how a responsible reviewer could establish whether the result is reliable."
    },
    "references": []
  },
  {
    "id": "think",
    "part": 0,
    "title": "Do enough of the thinking to direct the work.",
    "nav": "Think before you ask",
    "desc": "A rough first attempt gives you something to compare with AI's response. You need enough of your own understanding to recognize a useful suggestion, challenge an assumption, and decide when the work has improved.",
    "sources": [
      [
        "fall",
        "pp. 6–9"
      ],
      [
        "student",
        "pp. 11–12"
      ],
      [
        "short",
        "p. 2"
      ],
      [
        "slides",
        "pp. 8–13"
      ]
    ],
    "sections": [
      {
        "h": "Choose a first pass that fits the task.",
        "html": "<p>You do not need to finish a brief before asking AI to help with a heading. But you should understand the point that heading needs to make. Otherwise, a more forceful version can quietly change the argument, and you may not notice what you have traded away.</p>\n<p>The same principle applies at different stages of the work. Before seeking help with an outline, identify what the reader needs explained and which points matter most. Before asking for a critique of an argument, write down the argument and its strongest support. For a sentence edit, try to describe the problem: perhaps the sentence hides who acted, or asks the reader to hold an exception in mind for too long.</p>\n<p>Your first pass does not have to be impressive. It needs to be useful to you. It establishes what you think before another answer enters the conversation and gives you a more specific way to ask for help.</p>\n"
      },
      {
        "h": "Make your own assessment before receiving feedback.",
        "html": "<p>Before feedback arrives, write down your current answer. Identify the strongest and weakest parts of the reasoning, the authority or fact still needing attention, and the kind of feedback that would help most. Those are the five questions in the four-minute pause from the short guide.</p>\n<p>The value is the comparison that follows. A suggested revision may address a weakness you already recognized. It may reveal a problem you missed. Or it may sound convincing without answering the concern that matters. Mark an important suggestion as something to accept, modify, or reject, and give a reason. That small explanation makes your decision visible to you.</p>\n<p>For example, suppose you believe the client's current evidence does not establish receipt of notice. A suggested opening says the cure period has expired. Your preliminary assessment gives you a reason to question the change immediately. Another response may identify a source you overlooked. You can then examine that source and explain why your view changed rather than treating the new answer's confidence as the reason.</p>\n<p>Four minutes is a suggested practice, not an established threshold for legal performance. The short guide refers to research with science students and expressly notes that it does not establish the same effect in law school. Use the pause as a way to develop and compare your judgment. The optional worksheet provides a place to record the answers; the method does not depend on using the form.</p>\n"
      },
      {
        "h": "Different priorities can produce different investigations.",
        "html": "<p>The employee-departure problem makes the importance of a first pass visible. Read the supplied facts as a worked example rather than a question with one established legal answer:</p>\n<div class=\"gf-example\" data-reading-example=\"true\"><header><h3>The supplied employee-departure facts</h3></header><div class=\"gf-example-body\"><p>A former sales director signed a confidentiality agreement and a 12-month nonsolicitation clause. The clause allows her to accept business if the customer initiates contact. At 11:52 p.m., three days before resigning, someone using her credentials exported a spreadsheet listing 214 customers, renewal dates, discounts, margins, and pipeline notes. Minutes later, she texted a coworker: “I grabbed the whole playbook before they shut me out.” The company let every sales director export that data, did not use two-factor authentication, and another director sometimes logged in under her credentials.</p><p>Within two weeks at a competitor, she spoke with four former accounts. Two customers say they contacted her first after seeing her LinkedIn update. None of the four renews in the next 90 days. One competitor proposal used the same odd pricing label and typo found in one of the company’s internal templates. The company learned of her action on March 1, sent a demand letter on March 3, and waited until April 14 to file. It has declarations from IT and a vice president, but none from any customer. The company asks the court to bar her from working on any healthcare account, turn over every device used since resignation, and stop all contact with company customers. The competitor already imaged her laptop and says no company files were found.</p></div><p class=\"gf-source-caption\">Source: Leveling Up Your AI Prompting, slides 11–13. No controlling law is supplied.</p></div>\n\n<p>The response shown in the workshop foregrounds the export using the director's credentials, her message about taking the playbook, and her contact with former accounts. Those facts give the company a narrative worth investigating. But other facts point toward different questions. Another director sometimes used the credentials. The agreement permits customer-initiated business. The company delayed before filing, and the requested relief is broader than a ban on soliciting identified customers.</p>\n<p>A lawyer might therefore begin with attribution, the contractual exception, the urgency of the requested relief, or its breadth. Each priority changes the next assignment. A focus on attribution calls for evidence of who used the account. A focus on the exception calls for better evidence of who initiated contact. A focus on the requested order asks how its scope connects with what the company can establish.</p>\n<p>I have used this hypothetical with lawyers and judges, and their priorities vary. That disagreement matters because AI can present a selected ranking as though the assignment had a natural starting point. Your task is to examine the ranking, not accept it as a substitute for deciding what matters. The supplied packet has no controlling law that resolves the dispute, so neither the workshop's response nor this discussion establishes who should win.</p>\n"
      },
      {
        "h": "Return to the problem after considering the suggestions.",
        "html": "<p>Try a second pass after AI has expanded or challenged your initial view. Set its response aside for a moment and reconsider the client's question. What deserves more attention now? What has disappeared from the analysis? What alternative can you develop that the response did not offer?</p>\n<p>In workshops, I ask participants to add at least one approach beyond the AI's menu. That requirement is an exercise in independent thinking, not a claim that every novel idea will be better. It creates a reason to keep investigating after the system has produced an apparently complete answer.</p>\n<p>You may ultimately adopt much of the response. The important work is deciding why. Keep the suggestions that survive examination, revise those that need qualification, and discard the ones that do not fit the sources or the client's circumstances.</p>\n\n<p>The longer source guide calls this a <strong>divergence rule</strong>: produce an initial human list, ask AI to expand and challenge it, and make a second human list containing at least one approach the model did not supply. The point is to protect room for a different idea after an apparently complete answer arrives.</p>\n<p>The same guide describes other forms of purposeful friction. Ask for an adverse authority, a skeptical reader's objection, or an implementation failure before settling on a recommendation. Treat unsupported propositions as hypotheses until they have reviewed support. Create distance between generation and consequential reliance through a fresh-reader pass, another lawyer, or a later verification session. Record where your judgment changed the response. Each step protects something particular; it is not extra process for its own sake.</p>\n"
      },
      {
        "h": "Ask for help that makes you work through the question.",
        "html": "<p>An AI tool can be useful before it produces any replacement prose. Ask it to question your reasoning, point you toward a passage worth rereading, or explain why a distinction matters. Then attempt the next step yourself.</p>\n<div class=\"prompt-box\"><div class=\"prompt-top\"><span>Instructions to adapt</span><button class=\"text-btn\" data-copy-parent=\".prompt-box\">Copy instructions</button></div><pre>I have read the supplied materials and written the answer below. Ask me a question about the weakest part of my reasoning, then wait for my response. Point me to the relevant source passage so I can work through the issue myself. Distinguish what the source establishes from an inference you are drawing. Do not write a replacement answer yet.\n\nPermitted materials: [identify them].\nMy answer: [paste your attempt].</pre></div>\n<p>This approach is useful when learning a doctrine, but it also fits an experienced lawyer entering an unfamiliar area. You need to know which parts of the explanation you understand and which you are merely repeating. Continue practicing important skills without AI as well, especially when your work or course will require you to perform independently.</p>\n"
      }
    ],
    "quiz": {
      "q": "You have made an initial issue list and asked AI to challenge it. What would complete the exercise in independent thinking?",
      "a": [
        "Choose the AI’s most persuasive alternative and explain why you prefer it.",
        "Reconsider both lists and add at least one approach that the AI did not suggest.",
        "Ask the AI to combine the two lists into a final set of priorities."
      ],
      "correct": 1,
      "why": "Comparing alternatives is useful, but the exercise also asks you to create something beyond the options already supplied. The final pass should make room for your own judgment."
    },
    "references": []
  },
  {
    "id": "ethics",
    "part": 0,
    "title": "Take responsibility for the work you use.",
    "nav": "Responsibility and review",
    "desc": "Professional duties become useful when they change how you handle an assignment. Decide what information the tool may receive, what review the result needs, and who may approve the next action.",
    "sources": [
      [
        "fall",
        "p. 8"
      ],
      [
        "student",
        "pp. 10–11"
      ],
      [
        "short",
        "pp. 1–2"
      ]
    ],
    "sections": [
      {
        "h": "Turn a professional duty into a decision about the work.",
        "html": "<p>Suppose you want AI to summarize a client's correspondence. Before uploading it, you need to establish whether that use is authorized and whether the system is appropriate for the information. Paying for an account does not answer either question. You may need help understanding access, retention, and the provider's terms before making the decision.</p>\n<p>Other duties affect what happens after the response arrives. Competence requires enough understanding of the tool and the work to assess its contribution. Candor and accuracy require attention to what you present as supported. Supervision requires someone to direct and review delegated work. Communication and fee obligations affect what you tell the client and how you charge for the service. Your judgment remains necessary when choosing a recommendation among legally and practically different options.</p>\n<p>The ABA's Formal Opinion 512 provides a useful discussion of these duties under the Model Rules. It is guidance, not a replacement for the rules and authorities governing your jurisdiction or matter. Check applicable court requirements, client commitments, and organizational policies as well. In a course or clinic, follow the assignment and supervision requirements in addition to any professional obligations that apply.</p>\n\n<p>It helps to give each duty an operational meaning. Confidentiality affects data selection, access, retention, and the environment you use. Communication affects what the client needs to know under the rules, agreement, and circumstances. Supervision affects policies, training, responsibility for review, and the point at which work may proceed. Independent judgment calls for practical, economic, moral, social, and human considerations alongside the law. A system can help gather or explain those considerations without deciding their relative importance for the client.</p>\n"
      },
      {
        "h": "Check the proposition, not just the citation.",
        "html": "<p>Finding the cited case is the beginning of a source check. Read the passage that supposedly supports the point. Is it the court's conclusion, a description of another case, or an argument the court rejects? Does surrounding language limit the proposition? Then complete the validity and jurisdictional checks the intended use requires.</p>\n<p>Factual review needs the same care. An email may establish that a notice was sent without establishing receipt. A witness may describe something they were told without establishing that it occurred. Preserve those distinctions in the draft instead of treating every sentence in the record as equally certain.</p>\n<p>The appropriate review depends on the task and the basis you have for trusting the process. A new analytical use calls for different scrutiny from a narrowly defined task you have tested repeatedly. Opinion 512 expressly recognizes that review can vary with the tool and the assignment. For the exercises here, work closely with the supplied material so you can learn what a meaningful check involves. A second AI's agreement should never be mistaken for the underlying evidence.</p>\n"
      },
      {
        "h": "Make approval a step someone can actually perform.",
        "html": "<p>“Ask before sending” is a useful instruction, but an instruction alone does not establish that the software will prevent an email from going out. Check how the application's permissions work. Test whether the action remains blocked when approval is absent.</p>\n<p>Approval also needs an object. Which version did the reviewer approve, and for what use? Approving a draft for further discussion differs from approving it to be sent to the client. Supplying a missing document does not approve the new conclusion drawn from that document.</p>\n<p>For a manually run process, you can control the handoff: review the work, resolve the open questions, then start the next task. As more steps become automated, keep those decisions visible. Someone should be able to tell where review happened and what the reviewer allowed to proceed.</p>\n"
      },
      {
        "h": "Describe your use accurately when a record is needed.",
        "html": "<p>Keep a record proportionate to the assignment and its requirements. The useful details are what the system did, which materials mattered, how you checked the contribution, and what you changed. Avoid stock language that claims a more extensive review than you performed.</p>\n<div class=\"prompt-box\"><div class=\"prompt-top\"><span>Instructions to adapt</span><button class=\"text-btn\" data-copy-parent=\".prompt-box\">Copy instructions</button></div><pre>I used [tool and version, if known] to [specific purpose]. I supplied [general description of permitted materials]. I independently checked [identify what you checked], accepted or revised [describe material contributions], and take responsibility for the final work.</pre></div>\n<p>Use this wording only when a use note is appropriate, and adapt it to the applicable disclosure requirements. A statement that you verified an authority cannot make up for failing to open it. Likewise, an accurate description of AI use does not make an otherwise prohibited use permissible.</p>\n<p>Keep billing accurate, too. Time-based billing should reflect time actually worked, not the hours a task might have taken without AI. Other fee arrangements still need to comply with the governing rules and agreement.</p>\n"
      },
      {
        "h": "Direction from someone else does not settle your responsibility.",
        "html": "<p>A supervising lawyer asks for an AI-generated case summary before you have opened the opinion. The client may act on it that afternoon. The problem is not solved by noting who requested the summary. You still need to identify what has and has not been checked and what can responsibly be sent.</p>\n<p>The source guide points to Model Rule 5.2 for the principle that a subordinate lawyer remains bound by professional rules despite another person's direction. The full rule also addresses a supervisory lawyer's reasonable resolution of an arguable question of professional duty; applying it requires the actual rule and the relevant facts. This example does not resolve a jurisdiction-specific professional-responsibility question.</p>\n<p>The practical communication should explain the unresolved issue and the proposed next step. You might tell the supervisor that the holding has not yet been checked, describe the review you can complete, and distinguish any interim status report from advice based on the unchecked summary. The same discipline applies when an instructor, client, or system presses for an answer that exceeds what you can support.</p>\n<p>An accurate use note cannot cure inadequate review. It records what you did and what you relied on. The work must still meet the substantive standard for its intended use.</p>\n"
      }
    ],
    "quiz": {
      "q": "You need to disclose your use of AI. What should the disclosure say?",
      "a": [
        "That AI was involved, so readers should independently check the work.",
        "That the tool generated the draft and is responsible for any errors.",
        "What you actually used the tool for and what you checked, without suggesting that disclosure replaces those checks."
      ],
      "correct": 2,
      "why": "The use note should describe what happened. It cannot establish that a source was verified when you did not read it, and it does not shift responsibility for the final work."
    },
    "references": [
      {
        "title": "ABA Formal Opinion 512 (2024)",
        "url": "https://www.americanbar.org/content/dam/aba/administrative/professional_responsibility/ethics-opinions/aba-formal-opinion-512.pdf"
      },
      {
        "title": "ABA Model Rule 5.2: Responsibilities of a Subordinate Lawyer",
        "url": "https://www.americanbar.org/groups/professional_responsibility/publications/model_rules_of_professional_conduct/rule_5_2_responsibilities_of_a_subordinate_lawyer/"
      }
    ]
  },
  {
    "id": "method",
    "part": 1,
    "title": "Use the conversation to develop better work.",
    "nav": "Work through the exchange",
    "desc": "Your own skills give the exchange direction. These six practices explain how to develop alternatives, challenge an idea, and improve the work across more than one response.",
    "sources": [
      [
        "slides",
        "pp. 8–35"
      ],
      [
        "fall",
        "p. 4"
      ],
      [
        "short",
        "p. 1"
      ]
    ],
    "sections": [
      {
        "h": "Build the exchange around six working practices.",
        "html": "<p>Good prompting begins with how you do the work. A request cannot supply a priority you have not chosen or a standard of good writing you cannot recognize. My six working practices connect your own contribution with the kinds of assistance AI can offer.</p>\n<h3>First, do some work.</h3>\n<p>The first pass gives you a view to compare with the response. For a sentence, identify what makes it difficult to read. For an outline, decide what the reader needs explained and which issues matter most. For analysis, develop enough of the rule and facts to recognize a useful challenge. The amount varies; the reason stays the same. You need a basis for directing and evaluating the contribution.</p>\n<h3>Direct with guidance and examples.</h3>\n<p>Describe what should improve, supply the context, and show a useful example. A heading might work because it states a complete proposition, identifies who acted, and connects the action with the legal point. Tell the system that. Otherwise, “make it persuasive” leaves it to invent your standard, and “write like this” leaves it to choose which features of the sample to copy.</p>\n<h3>Choose with options and iterations.</h3>\n<p>Ask for alternatives that expose a decision. Different openings can begin with the client's objective, the decisive fact, or the consequence of an unresolved condition. Compare the emphasis and the cost of each choice. Then identify what the next round should preserve and what it should change. The first response becomes material for further work rather than a finished answer you must either accept or discard.</p>\n<h3>Lean on expansion, pressure testing, and identification.</h3>\n<p>These are different assignments. Expansion asks what else might matter or support an idea. Pressure testing asks what a strong opponent, skeptical judge, or affected client would say against it. Identification asks the system to locate a specified feature: sentences containing several ideas, unexplained jargon, unsupported steps, or passages where the reader may lose the thread. You can ask for this work without requesting replacement prose.</p>\n<h3>Scale the work for yourself and the AI.</h3>\n<p>A large request can overwhelm the review as well as the generation. If the system reorganizes, rewrites, and adds analysis across ten pages, you have to detect several kinds of change at once. A defined issue, paragraph, heading, or source comparison may give you a more useful unit. Keep connected questions together when separating them would distort their relationship. The aim is a manageable amount of work, not the smallest possible prompt.</p>\n<h3>Prompt in a way that incorporates those decisions.</h3>\n<p>The final request should reflect the choices that this task needs. It may include your first attempt, the relevant sources, a sample with an explanation, and a request for alternatives before drafting. Another task may need only a focused comparison and a clear limit. The practices are a way to conduct the work, not a requirement to write six messages or fill six boxes every time.</p>\n"
      },
      {
        "h": "Ask for alternatives that expose a writing decision.",
        "html": "<p>Five versions of the same sentence may differ only in their verbs. Sometimes that is useful. But for a heading or opening paragraph, ask for alternatives that help you examine the point you are making.</p>\n<p>Suppose the recommendation depends on an unresolved fact. One opening could lead with the inability to confirm the answer. Another could begin with the information the client needs to provide. A third might explain the practical risk of proceeding before that information arrives. All can preserve the same substance while directing the reader's attention differently.</p>\n<p>Ask the tool to explain those differences, then examine the explanations yourself. Which version helps this reader make the decision? Which one might imply greater certainty than the evidence supports? After choosing, tell the system what to preserve. Otherwise, the next rewrite may reopen a choice you have already made.</p>\n\n<p>Ask for the pros and cons of the alternatives, but examine those explanations too. A model may call every version “clearer” without identifying what actually changed. Press for a contrast you could disagree with: one version foregrounds uncertainty, another identifies the next action sooner, and a third gives more factual context before the recommendation. Now you have a decision to make.</p>\n<p>You can also request alternatives to an analytical frame. After reading an opinion, explain the rule you think matters and ask which other rules or distinctions deserve consideration. After developing an argument from a particular passage, ask what other language or facts could bear on that argument. The workshop's research examples use assistance repeatedly within the process, rather than once at the beginning of research and once at the end of drafting.</p>\n"
      },
      {
        "h": "Make the follow-up as specific as the problem.",
        "html": "<p>When a revision almost works, identify where it succeeds before explaining what remains wrong. This helps you preserve a useful change instead of restarting the whole passage.</p>\n<div class=\"prompt-box\"><div class=\"prompt-top\"><span>Instructions to adapt</span><button class=\"text-btn\" data-copy-parent=\".prompt-box\">Copy instructions</button></div><pre>The opening now makes the recommendation easy to find, but it treats the notice date as settled. Keep the opening&#x27;s organization. Explain that the record establishes sending, not receipt, and connect that gap to the next step. Do not invent a receipt date or imply that the other termination requirements are satisfied.</pre></div>\n<p>Compare that with “try again, but be more careful.” The specific instruction tells the tool which fact needs attention, what meaning must survive, and which part of the draft you have accepted. It also gives you a focused question for reviewing the next response: did it preserve the sending–receipt distinction without undoing the useful opening?</p>\n<p>A follow-up can question the analysis, too. Ask why a proposed distinction matters or which source supports an inference. The conversation should help you investigate the work, not merely cycle through more polished versions.</p>\n\n<p>A useful follow-up can preserve a small writing success. “The verb here works, but the subject is vague” is enough to direct the next round toward a specific problem. You may also combine parts of two options, ask for a different emphasis, or stop revising because the passage already does its job. Producing another version is not an improvement by itself.</p>\n"
      },
      {
        "h": "Keep each round small enough to review.",
        "html": "<p>A request to rewrite ten pages can change the argument, organization, and wording at once. Even a capable response leaves you with a demanding comparison. You need to recognize which changes improve the document and which alter something that should remain.</p>\n<p>Choose a unit that lets you make those decisions. You might settle the order of the issues before drafting paragraphs, or work on the headings before revising the analysis beneath them. For a dense provision, first identify the condition and exception, then ask how to explain their relationship to the client.</p>\n<p>Smaller is not automatically better. An exception should not be separated from the rule it qualifies, and related agreements may need to be read together. The right size is the amount of work you can meaningfully direct and check. Increase it when your testing and experience give you a sound reason to do so.</p>\n"
      },
      {
        "h": "Keep the five-stage process distinct from the six practices.",
        "html": "<p>The <strong>responsible-use operating system</strong> in the longer source guide describes the whole assignment. Its stages have different jobs from the six practices for conducting an exchange.</p>\n<p>The <strong>human-first frame</strong> establishes the objective, issues, decision points, and initial theory before the model supplies them. <strong>AI-assisted expansion</strong> develops that starting work through alternatives, comparison, structure, simulation, critique, or authorized drafting. The <strong>lawyer-grade audit</strong> examines authority, quotations, facts, procedural posture, reasoning, instructions, data handling, and the strongest counterargument. It is broader than confirming that citations exist.</p>\n<p><strong>Human revision and judgment</strong> is where you accept, reject, combine, and rewrite, then decide what should be used and why. <strong>Document and improve</strong> records the purpose, sources, significant output, checks, rejected suggestions, and process lesson when the assignment or risk warrants it. A useful lesson should change the next workflow rather than remain buried in a chat.</p>\n<p>The five-question before-use check comes earlier: it asks whether the use is appropriate at all. The ten prompting principles in the next chapter help specify an individual assignment. The agent work order makes a longer delegation explicit. These frameworks do not compete for the same role. The guide explains each where it is useful so you can choose the one that addresses the decision in front of you.</p>\n"
      }
    ],
    "quiz": {
      "q": "An AI revision improves the opening but treats a disputed fact as settled. Which response gives it the most useful direction?",
      "a": [
        "Ask for a more careful revision of the entire passage.",
        "Keep the opening, identify the disputed fact, and explain how the next revision should qualify it.",
        "Request several alternatives and choose the one that sounds least certain."
      ],
      "correct": 1,
      "why": "Specific feedback identifies both the useful change and the problem to correct. You still need to check the next version against the record; a general reduction in certainty may not fix the particular overstatement."
    },
    "references": []
  },
  {
    "id": "prompting",
    "part": 1,
    "title": "Give the AI an assignment it can act on.",
    "nav": "Write a useful prompt",
    "desc": "A useful prompt explains what you need and why. It supplies the relevant material, identifies the limits, and describes a result you can review.",
    "sources": [
      [
        "slides",
        "pp. 14–19, 32–39"
      ],
      [
        "student",
        "pp. 5–6"
      ]
    ],
    "sections": [
      {
        "h": "Explain what the work is supposed to accomplish.",
        "html": "<p>“Summarize this contract” leaves the purpose open. A client deciding whether to sign may need to understand obligations and practical risks. A lawyer preparing for a termination dispute may need a much narrower account of notice requirements, cure rights, and remedies. The same agreement calls for different work.</p>\n<p>Begin with that distinction. Tell the system who will use the result and what decision it should support. Identify the materials it may use, including any document that changes another. Where it matters, give your current view so the tool can engage with your reasoning rather than start from an unspecified position.</p>\n<p>Then describe what you need back. A source-linked comparison table may be easier to review than a finished recommendation. A set of questions may be more useful than a first draft. Choosing the form of the response is part of designing the assignment.</p>\n"
      },
      {
        "h": "Use the ten principles to explain the assignment.",
        "html": "<p>I use ten prompting principles to explain the choices behind a useful request. Each addresses a practical source of misunderstanding. They are choices to make when the task calls for them, not a fixed format that every request must follow.</p>\n<h3>1. Provide the role and audience.</h3>\n<p>Identify the perspective that would help and the person who needs the result. A skeptical reviewer has a different job from a client counselor. A client unfamiliar with a doctrine needs a different explanation from a specialist. A grand title does not create expertise; the useful part of the role is the assignment it clarifies.</p>\n<h3>2. Provide context, data, and goals.</h3>\n<p>Explain what the work should accomplish, which facts and documents matter, and what you have already decided. A summary intended to orient a new colleague may differ from one prepared to evaluate a single contractual condition. State the primary goal and any secondary goal whose tradeoff needs attention.</p>\n<h3>3. Use annotated examples.</h3>\n<p>Supply an example and explain the choice that makes it useful. It may use a concrete subject, put the answer before the background, or preserve a difficult qualification without burying the point. Say which features should transfer and which facts or wording must stay behind.</p>\n<h3>4. Use menus, expansion, and pressure testing.</h3>\n<p>A menu of meaningful options gives you alternatives to judge. Expansion can reveal an omitted reason, issue, or explanation. Pressure testing challenges the position with the best available objection. Ask for supporting material where the suggestion depends on facts or law. An invented counterargument is not more useful because it sounds forceful.</p>\n<h3>5. Set parameters for the result.</h3>\n<p>Describe the form that will help you use and check the response. You may need a source-linked table, a paragraph of advice, or headings that each state a proposition. Include the necessary scope and level of detail. A word count may constrain a task, but it does not explain what information deserves the space.</p>\n<h3>6. Iterate with follow-ups.</h3>\n<p>Tell the system which parts you accept and which need another round. “Keep the opening, but put the missing factual condition beside the recommendation” preserves a useful choice while directing a change. Avoid restarting the whole task when only one part is unresolved.</p>\n<h3>7. Break down the steps and stay organized.</h3>\n<p>When one task needs a reviewed result from another, state that sequence. For example, extract a source's relevant proposition, compare it with your intended use, and only then draft a heading. The useful result is observable intermediate work you can examine. You do not need to treat a displayed account of the model's internal reasoning as evidence of correctness.</p>\n<h3>8. Use AI to help improve your prompts.</h3>\n<p>Describe a result you liked and why, then ask for reusable instructions that would pursue those features on another assignment. Or ask the system to identify ambiguity in your proposed request before starting. Review the resulting prompt yourself. The system can make your unstated assumption more polished without making it right.</p>\n<h3>9. Reset and reuse.</h3>\n<p>Keep instructions that worked alongside the source requirements, examples, and limitations that made them useful. For a new matter, replace the old facts and confirm the applicable scope. In a long exchange, a fresh start with an accurate continuation record may be better than repeatedly appending qualifications to outdated directions.</p>\n<h3>10. Avoid AI-isms.</h3>\n<p>Give positive direction as well as identifying habits to avoid. Explain the audience, desired emphasis, and useful examples. Ask for connected prose where reasoning needs development, familiar words where jargon adds nothing, and substantive engagement with the facts. Removing conspicuous vocabulary will not supply a missing analysis; the editing chapter develops that distinction.</p>\n"
      },
      {
        "h": "Explain what an example demonstrates.",
        "html": "<p>A sample heading might work because it names the person who acted and explains why the action matters. A client email might begin with the decision the client needs, then develop the reason in an order the client can follow. Name that choice when you provide the example.</p>\n<p>Without the explanation, “write like this” asks the model to decide which features to copy. It might imitate a phrase you barely noticed while missing the organization that made the sample useful. It might also import facts or legal propositions that belong only to the example.</p>\n<div class=\"prompt-box\"><div class=\"prompt-top\"><span>Instructions to adapt</span><button class=\"text-btn\" data-copy-parent=\".prompt-box\">Copy instructions</button></div><pre>Use the sample to learn how the writer introduces the dispute: it identifies who acted, explains the concrete conduct, and connects that conduct to the question the reader needs answered. Apply that approach to my passage. Do not copy the sample&#x27;s facts, legal propositions, or distinctive phrases. Preserve every material qualification in my passage.</pre></div>\n<p>Examples can teach analysis as well as style. You might show how a strong paragraph connects particular facts to a rule, then ask the system to identify where your draft leaves that connection unexplained. Be precise about what the example is evidence of. It demonstrates a technique; it does not establish the law of the new matter.</p>\n"
      },
      {
        "h": "Choose the variables that matter to this task.",
        "html": "<p>A useful reusable prompt leaves the changing parts visible. Audience, primary and secondary goal, tone, format, examples, and limits may all vary. Do not preserve an old request's four-bullet structure merely because it once worked for a different email.</p>\n<p>Describe priorities explicitly. When readability and a material qualification pull in different directions, say that the qualification must survive and ask for ways to explain it more clearly. At the end of a long request, a brief restatement of the main objective can help keep your own instructions coherent. That is an organizing habit, not a guarantee that the system will follow every direction.</p>\n<p>Give quoted material a defined role. Tell the tool whether a passage is source evidence to preserve, a draft to revise, or a style example whose facts do not belong in the new work. In legal writing, specify that quotations and citations must not be silently altered. Quotation marks alone are not a reliable substitute for those directions.</p>\n<p>The workshop also suggests making stylistic preferences explicit. Its example uses weighted traits and numerical targets for directness or sentence length. Treat those as possible prompt variables, not a formula for good writing. For this guide, the more useful instruction is to vary the rhythm naturally, explain the reasoning in full sentences, and let the material determine the paragraph. A repeated short–short–long pattern would defeat that aim.</p>\n<p>Here is a prepared request that combines several of these choices without making the form the point:</p>\n<div class=\"prompt-box\"><div class=\"prompt-top\"><span>Example instructions</span><button class=\"text-btn\" data-copy-parent=\".prompt-box\">Copy instructions</button></div><pre>Revise the client email below using only the supplied information. The client needs to decide whether to provide the missing support before Friday. Put that decision and the reason near the beginning. Preserve the distinction between a condition we cannot yet confirm and a condition that has failed.\n\nOffer two versions that organize the explanation differently. Explain what each helps the reader see and flag any change that might affect meaning. Use connected paragraphs, not a list unless the information genuinely needs one. Keep the quoted contractual language unchanged.\n\nEmail and source material: [supply the permitted material].</pre></div>\n<p>This example was prepared for the guide. It illustrates the workshop's instruction choices; it does not add a new factual record or establish the right recommendation in a live matter. The optional prompt builder helps organize the same choices for an assignment you bring.</p>\n"
      },
      {
        "h": "Review the proposed approach before substantial work begins.",
        "html": "<p>For a larger assignment, ask the system to describe its plan before drafting. This gives you an early opportunity to correct a mistaken assumption about the goal or a missing source.</p>\n<div class=\"prompt-box\"><div class=\"prompt-top\"><span>Instructions to adapt</span><button class=\"text-btn\" data-copy-parent=\".prompt-box\">Copy instructions</button></div><pre>Before you perform this assignment, explain how you understand the task. Identify material information that is missing or ambiguous, and propose a manageable approach using the permitted sources. Tell me which decisions you need me to make before proceeding. Wait for my response before drafting.</pre></div>\n<p>Review the plan against your own understanding. A tidy sequence can still be aimed at the wrong question. Once the plan fits, begin with the first useful task and check its result before moving forward. The next chapter shows how to make that sequence visible in a workflow map.</p>\n\n<p>A proposed self-check can also ask for verification questions that would expose an error, answers grounded in the supplied material, and a revision addressing the resulting problems. Keep the distinction between critique and verification clear. The model's ability to ask and answer its own questions can expose something worth checking; it does not independently establish the answer.</p>\n"
      }
    ],
    "quiz": {
      "q": "You give the AI a strong heading as an example. What should you explain about it?",
      "a": [
        "Which client name and factual details it should reuse.",
        "Which writing choices make the heading effective for this audience.",
        "That the example is authoritative enough to follow without further review."
      ],
      "correct": 1,
      "why": "An example can teach several different things. Pointing out the useful choices helps the AI distinguish the feature you want from details that belong only to the original assignment."
    },
    "references": []
  },
  {
    "id": "graphing",
    "part": 1,
    "title": "Map the work before you ask AI to carry it out.",
    "nav": "Map an AI workflow",
    "desc": "Graphing an AI workflow means showing the tasks, what passes between them, and the decisions that determine what happens next. You can begin with a work plan on paper and run each step yourself.",
    "sources": [
      [
        "graph",
        "sections 1–10"
      ],
      [
        "fall",
        "pp. 10–14"
      ]
    ],
    "sections": [
      {
        "h": "A workflow map makes the assignment easier to supervise.",
        "html": "<p>Imagine asking AI to review a contract, read the correspondence, and recommend whether the client should terminate. That request leaves many decisions inside a single exchange. Which provisions matter? What does the correspondence establish? What should happen when a necessary fact is missing?</p>\n<p>A workflow map brings those decisions into view. Each box names a task. A connecting line shows that one task needs something from another. A branch shows that the next step depends on what you find. For example, missing evidence might send the work back for investigation instead of forward to drafting.</p>\n<p>The unfamiliar term is <strong>graph</strong>; the underlying skill is planning an assignment. Prompts give instructions for particular tasks. The map explains how those tasks fit together. A person can perform a task, an AI system can assist with it, or ordinary software can handle it. You do not need several AI agents to benefit from the plan.</p>\n"
      },
      {
        "h": "Begin with a defined question and appropriate materials.",
        "html": "<p>We will use a fictional software-vendor matter. The client has reported service failures and wants advice about its options. The working materials include an agreement, an amendment, correspondence, and service records. For this example, assume the lawyer has also supplied the relevant governing-law analysis. Reviewing the contract alone would not resolve every legal question in an actual termination dispute.</p>\n<p>The initial work plan separates two tasks. One identifies the contractual requirements. The other builds a factual timeline. Their findings then come together for a comparison that the lawyer reviews before choosing the approach to the recommendation.</p>\n<p>Here is the important gap: the fictional contract measures the cure period from <strong>receipt</strong> of written notice, but the initial packet establishes only that an email was <strong>sent</strong>. The workflow needs somewhere for that difference to become visible and someone responsible for deciding what to do about it.</p>\n"
      },
      {
        "h": "Follow the reasoning from the sources to the recommendation.",
        "html": "<p>The map begins with the lawyer's objective. It then separates contract review from factual review, brings the findings together, and returns the important decisions to the lawyer. Here is the complete sequence in readable form:</p>\n<div class=\"gf-table-wrap\" tabindex=\"0\" role=\"region\" aria-label=\"A readable version of the fictional vendor-review workflow.\"><table class=\"gf-reading-table\"><caption>A readable version of the fictional vendor-review workflow.</caption><thead><tr><th scope=\"col\">Task</th><th scope=\"col\">What the work produces</th><th scope=\"col\">What happens next</th></tr></thead><tbody><tr><td>Define the question</td><td>The client’s objective, approved materials, and the decision the work should support.</td><td>The lawyer selects the scope before the reviews begin.</td></tr><tr><td>Review the contract and amendment</td><td>A requirements table with the relevant language, exceptions, source locations, and open questions.</td><td>These findings go to the comparison, not directly to a final recommendation.</td></tr><tr><td>Review records and correspondence</td><td>A timeline distinguishing established evidence, allegations, disputed facts, and missing information.</td><td>It preserves the distinction between sending and receipt.</td></tr><tr><td>Compare the findings</td><td>Each requirement is connected with its supporting evidence or a stated gap.</td><td>A material gap returns to the lawyer for a decision.</td></tr><tr><td>Resolve the next step</td><td>The lawyer decides whether to investigate, seek more material, or approve a qualified approach.</td><td>New evidence alone does not count as approval.</td></tr><tr><td>Draft the recommendation</td><td>A draft using approved findings and the lawyer’s decisions, with material limits preserved.</td><td>The draft goes through a source check and human review.</td></tr><tr><td>Check and approve</td><td>Unsupported assertions and lost qualifications are corrected; the lawyer decides what may be used.</td><td>A material problem returns the affected work for correction.</td></tr><tr><td>Revisit when evidence changes</td><td>The timeline, comparison, and recommendation are reconsidered as needed.</td><td>Reviewed work is reused only where the change does not undermine it.</td></tr></tbody></table></div>\n\n<p>The first two reviews can begin separately because they answer different initial questions. The contract task identifies the applicable requirements; the record task establishes what the available evidence shows. The comparison needs both results. Drafting needs the reviewed comparison and the lawyer's chosen approach.</p>\n<p>Suppose the correspondence shows an email sent on June 4 but does not establish receipt. The comparison should identify a material gap because the fictional contractual period runs from receipt. It should not insert June 4 into the calculation merely because that is the only date available. The lawyer might seek an acknowledgment, ask for additional evidence, or approve a recommendation that expressly preserves the uncertainty. Those choices are different from a finding that the period has expired.</p>\n<p>Later, an acknowledgment of receipt arrives. The timeline can be updated, the comparison reconsidered, and the recommendation revised. The new date does not automatically establish that every other contractual condition is met. It also does not count as the lawyer's approval. This is why the map separates new information, analysis, and authorization to proceed.</p>\n<p>The interactive demonstration lets you move through the same sequence, but the reasoning above is the lesson. A workflow is useful when it makes necessary work and decisions visible, not merely because the diagram looks orderly.</p>\n"
      },
      {
        "h": "Give each task a result the next person can use.",
        "html": "<p>A box labeled “Analyze the contract” is a start, but it leaves the assignment vague. Explain the question, identify the permitted materials, and describe what should come out of the task. Include what to do when the task cannot be completed as requested.</p>\n<p>For the initial contract review, the assignment could require a table identifying each relevant termination condition, the language supporting it, and its source location. The table should preserve exceptions and point out any missing referenced material. It should not yet conclude that the client has met the conditions.</p>\n<p>Now the next reviewer knows what they are receiving. They can compare a requirement with the factual record, inspect the supporting provision, and see which questions remain unresolved. This is what a useful handoff accomplishes: it preserves enough of the work for someone else to examine and continue it.</p>\n<p>The task's review requirement should be equally concrete. Before the findings are used in a recommendation, the lawyer checks the relevant provisions and resolves material questions about how the agreement and amendment fit together.</p>\n"
      },
      {
        "h": "Keep the initial source review separate from the recommendation.",
        "html": "<p>The contract review asks what the documents require. The timeline asks what the records show happened. Keeping those initial jobs distinct helps you inspect the basis for the later comparison.</p>\n<div class=\"prompt-box\"><div class=\"prompt-top\"><span>Instructions to adapt</span><button class=\"text-btn\" data-copy-parent=\".prompt-box\">Copy instructions</button></div><pre>Read the agreement and amendment together. Identify the provisions relevant to termination for the reported service failures. For each requirement, give the relevant language and location, including exceptions or qualifications. Identify uncertainty about how the provisions fit together and anything you could not review. Do not decide whether the client has satisfied the requirements yet.</pre></div>\n<div class=\"prompt-box\"><div class=\"prompt-top\"><span>Instructions to adapt</span><button class=\"text-btn\" data-copy-parent=\".prompt-box\">Copy instructions</button></div><pre>Build a timeline from the supplied records and correspondence. Cite the document and location supporting each entry. Distinguish what a source establishes from what someone alleges, and preserve conflicting accounts. Identify missing information. Do not treat evidence that notice was sent as evidence of receipt or conclude that a contractual requirement has been satisfied.</pre></div>\n<p>You can run these requests in ordinary chats, one after the other. Give each the shared assignment and the materials it needs. Save the useful outputs with their source references. When you ask for the comparison, provide both sets of findings and access to the originals. The map does not require automation; at this stage, you are managing the handoffs yourself.</p>\n"
      },
      {
        "h": "Pass the uncertainty forward with the finding.",
        "html": "<p>“Notice sent June 4” and “notice received June 4” are different findings. A handoff containing only “Notice: June 4” conceals that difference. The next task may calculate from the date without realizing what the evidence actually supports.</p>\n<p>Require the comparison to connect each proposed conclusion with a contractual requirement and supporting evidence. When the support is incomplete, say what remains missing. A later drafting request should receive that qualification along with the lawyer's decision about how to handle it.</p>\n<div class=\"prompt-box\"><div class=\"prompt-top\"><span>Instructions to adapt</span><button class=\"text-btn\" data-copy-parent=\".prompt-box\">Copy instructions</button></div><pre>Compare the contractual requirements with the factual findings. For each proposed conclusion, identify the supporting provision and record source. Preserve disputed facts and missing evidence. Do not resolve a material gap by assumption. Return the comparison and the questions the lawyer needs to decide before drafting advice.</pre></div>\n<p>Suppose the lawyer approves seeking an acknowledgment of receipt before recommending termination. That decision belongs in the next task's instructions. Otherwise, the drafting step may quietly replace it with a more confident conclusion. A short record of approved decisions can prevent the same issue from being reopened without anyone noticing.</p>\n"
      },
      {
        "h": "Separate tasks where separation improves the work.",
        "html": "<p>Ask what a task must receive before it can begin. The initial factual timeline does not require the completed contract analysis. The recommendation needs both, together with the lawyer's decisions. That dependency gives you a reason to delay drafting until the comparison has been reviewed.</p>\n<p>Separate work need not happen simultaneously. You can test the plan manually before considering software that runs suitable tasks at the same time. The first question is whether each task has a clear job and returns something useful.</p>\n<p>Be careful with issues that are closely connected. Reviewing several agreements separately may help you organize their provisions, but someone still needs to examine how they interact. A task map should make that combined review explicit. Dividing the work is useful only when the plan also brings the necessary relationships back together.</p>\n\n<p>Several arrangements recur. A sequence handles work that must follow earlier work. Separate reviews that later come together can give a comparison distinct findings to examine. A branch changes the next action based on what the earlier task found. A return path sends a draft back when a source check identifies an overstatement. The vendor example uses all of these without requiring a complicated system.</p>\n<p>A map of work is also different from a knowledge graph. A knowledge graph represents relationships in information, such as connections among people, events, and documents. A workflow map represents the tasks and decisions through which work proceeds. Both can be useful, but drawing one does not create the other.</p>\n"
      },
      {
        "h": "Define the final review before you rely on the draft.",
        "html": "<p>“Check your work” does not tell a reviewer what to compare or what would count as a material problem. For this recommendation, the reviewer needs the underlying sources, approved findings, and the lawyer's instructions.</p>\n<div class=\"prompt-box\"><div class=\"prompt-top\"><span>Instructions to adapt</span><button class=\"text-btn\" data-copy-parent=\".prompt-box\">Copy instructions</button></div><pre>Compare the draft with the underlying documents, approved findings, and my decisions. Identify unsupported assertions, omitted qualifications, and passages that treat an unresolved question as settled. For each issue, quote the draft language, identify the relevant source and location, and propose a correction or a question for me. Report anything you could not check.</pre></div>\n<p>Review the important findings yourself. An additional AI review can help identify a problem, but another generated assertion is not proof that the source supports the claim. Use an appropriate check for the question: arithmetic may need a calculator; a statement about receipt needs evidence; a recommendation needs judgment about what the client should do.</p>\n<p>Also decide when the revision cycle ends. You might allow a correction round after source review, then require the lawyer to resolve any remaining material issues. Repeatedly asking the system to review itself until it declares success gives you no independent stopping standard.</p>\n"
      },
      {
        "h": "Test the map before automating it.",
        "html": "<p>Compare your mapped approach with a simpler request using the same materials. Did the map expose a meaningful gap? Did it reduce overstatement? How much time did the lawyer spend checking and repairing the result? One successful example is a reason to keep testing, not a guarantee that the process will work on every matter.</p>\n<p>Then change the facts. When the new email establishes receipt, the timeline and comparison need updating, followed by reconsideration of the recommendation and final review. The contract extraction may remain useful, subject to checking whether the new evidence makes another provision relevant. This shows why a map can help with revisions as well as first drafts.</p>\n<p>Once the manual plan is useful, software may be able to manage the handoffs, save progress, or prevent a step from proceeding without approval. Those features must be implemented and tested. A diagram or an instruction to pause does not itself create an enforced restriction.</p>\n<p>The optional <a href=\"#/lab/process\">process worksheet</a> helps you plan an assignment of your own. Start with the smallest set of tasks that makes the work clearer. Add a step when you can explain what it contributes or what error it prevents.</p>\n"
      }
    ],
    "quiz": {
      "q": "The contract starts the cure period on receipt of notice, but the packet establishes only that an email was sent. What should happen next?",
      "a": [
        "Calculate from the sent date and mention the receipt issue in a footnote.",
        "Let the drafting task decide whether the missing date is important.",
        "Identify the missing evidence and seek the lawyer’s decision about further investigation or a qualified analysis."
      ],
      "correct": 2,
      "why": "The comparison should preserve the distinction between sending and receipt. The lawyer must decide how to handle the gap before later work treats an unproved date as established."
    },
    "references": [
      {
        "title": "Anthropic: Building effective agents",
        "url": "https://www.anthropic.com/engineering/building-effective-agents"
      }
    ]
  },
  {
    "id": "harness",
    "part": 1,
    "title": "Give the AI the right materials for the next task.",
    "nav": "Organize the materials",
    "desc": "A useful prompt can still produce poor work when the system has the wrong documents or an outdated account of the matter. Organize the information so you can tell what the tool should use and what it actually used.",
    "sources": [
      [
        "fall",
        "p. 14"
      ],
      [
        "student",
        "pp. 4–8"
      ],
      [
        "slides",
        "pp. 33–37"
      ]
    ],
    "sections": [
      {
        "h": "Build a working file that someone else could understand.",
        "html": "<p>Imagine handing a new colleague a folder of unsigned drafts, executed agreements, old comments, and email attachments. “Everything is in there” does not tell them which document controls or what you have already decided. An AI system needs that distinction, too.</p>\n<p>Begin with a short assignment document and a deliberate source collection. Identify the question, the current documents, and the result you need. Keep approved findings separate from unfinished proposals. You can do this in an authorized project workspace or with reference files supplied to each session; the exact arrangement depends on the product you use.</p>\n<p>You may hear this described as building a <strong>harness</strong> or doing <strong>context engineering</strong>. The terms concern the information and supporting system around the model. Organizing reference files is one useful part. It does not, by itself, enforce access limits or create a review process. Keep that distinction clear when someone claims that a folder of instructions makes a workflow safe.</p>\n\n<p>The source materials use <em>harness</em> in two related senses. One describes the software surrounding a model, including tools, memory, retrieval, and enforced controls. Another describes a working arrangement of instructions, files, examples, and checks that you organize for an assignment. A folder of references can improve that working arrangement. It does not by itself implement the permissions and enforcement features of software. When planning a use, specify which part you have actually built.</p>\n"
      },
      {
        "h": "Make the current version easy to identify.",
        "html": "<p>For the vendor matter, a useful working file would begin with the client's objective and the scope of the analysis. The signed agreement and amendment should be clearly identified as sources. A reviewed requirements table and timeline should retain their source locations and open questions.</p>\n<p>Keep writing examples apart from matter evidence. A strong brief used to demonstrate style should not become a source of facts or law for the vendor dispute. Likewise, a record of the lawyer's decisions should distinguish approved conclusions from ideas considered and rejected.</p>\n<p>You do not need an elaborate naming scheme. You do need names, dates, and a short explanation that make the distinctions apparent. “Notice timeline — reviewed September 8; receipt unresolved” tells the next task more than “Timeline final 2.” When something changes, identify what supersedes the earlier version and what needs to be reconsidered.</p>\n<p>For a recurring assignment, keep reusable instructions separate from the matter-specific file. That makes it easier to reuse the method without carrying another client's details into the new work.</p>\n\n<p>The source guide identifies ten elements worth organizing. <strong>Objective</strong> and <strong>context</strong> explain the job and the circumstances. A <strong>trusted source set</strong> defines the materials, and <strong>examples</strong> show the intended standard and common mistakes. <strong>Output structure</strong> makes the result easier to inspect. <strong>Sequence</strong> identifies the tasks and their dependencies.</p>\n<p>The remaining elements protect continued use: <strong>independent checks</strong>, <strong>escalation rules</strong>, <strong>logs and versions</strong>, and an <strong>evaluation set</strong>. A calculator, a source comparison, or a designated reviewer may perform different checks. Stop conditions return specified problems to a person. A version record identifies the instructions and sources used. Known-answer and boundary examples let you test whether a change improves the process or damages something that worked.</p>\n<p>These elements need not become ten files. What matters is that the functions are covered. In the vendor matter, the requirements table and timeline preserve the source support. A record of unresolved issues tells the drafting task what it may not assume. A small set of receipt scenarios tests whether the workflow treats missing evidence appropriately. Each item has a job beyond making the folder look organized.</p>\n"
      },
      {
        "h": "Check what the system found and how it read it.",
        "html": "<p>A retrieval system searches a collection for material relevant to the request. The resulting answer depends on both the search and the interpretation. Those are different opportunities for error.</p>\n<p>An accurate account of a termination provision may still be incomplete if the search missed an amendment. Conversely, retrieving the amendment does not establish that the model correctly understood how it changes the agreement. When reviewing a result, ask which documents support the important conclusions and whether any required source is absent.</p>\n<p>Make unreadable or unavailable material visible. Ask the tool to identify a document it could not access rather than quietly continue with the rest. For a material conclusion, preserve enough of the source location that you can examine the surrounding language. This turns a general assurance that the documents were reviewed into work you can inspect.</p>\n"
      },
      {
        "h": "Leave the next session an accurate account of the work.",
        "html": "<p>At the end of a substantial session, ask for a short continuation record. It should identify the current assignment, the source versions, and the findings you reviewed. It should also preserve unanswered questions and say what task comes next.</p>\n<div class=\"prompt-box\"><div class=\"prompt-top\"><span>Instructions to adapt</span><button class=\"text-btn\" data-copy-parent=\".prompt-box\">Copy instructions</button></div><pre>Prepare a record for the next session. State the current assignment and approved source versions. Summarize the reviewed findings with source locations, preserving disputed facts and unresolved questions. Distinguish my decisions from suggestions I did not approve. Identify the next task and what must be checked before it begins. Do not turn an unreviewed proposal into an accepted finding.</pre></div>\n<p>Read the record before reusing it. A summary can omit the very qualification you need it to preserve. In the vendor example, an account that says “notice requirements satisfied” would be misleading if receipt remains unresolved. Correct the summary while the distinction is still clear in your mind.</p>\n<p>The aim is that a new session, or another lawyer, can continue from an accurate account rather than reconstructing a long conversation and guessing which parts still apply.</p>\n"
      },
      {
        "h": "Connect the materials to the decisions they support.",
        "html": "<p>A well-organized file should make the next review easier. The requirements table points to the relevant contractual language. The timeline identifies the evidence. A note of unresolved questions tells the drafting task what it must not assume. The lawyer's decisions explain which approach has been approved.</p>\n<p>After using the process, record a recurring error where it can improve the next assignment. If the system repeatedly treats sent notice as received notice, revise the timeline instructions and add a test that checks the distinction. Keeping the mistake only in a chat history makes it easy to repeat.</p>\n<p>This is how the prompt, reference materials, workflow, and review begin to support one another. Each serves a different purpose. Together, they give you a more dependable way to direct the work than a longer prompt alone.</p>\n"
      }
    ],
    "quiz": {
      "q": "You are continuing an assignment in a new AI session. What should you provide?",
      "a": [
        "The latest draft, leaving the new session to infer how you reached it.",
        "The reviewed findings and decisions, the unresolved questions, and access to the sources needed for the next task.",
        "The entire conversation, without identifying which parts are still accurate."
      ],
      "correct": 1,
      "why": "The next task needs to know what it may rely on and what remains unresolved. Keep the underlying sources available so a summary does not become an unsupported substitute for them."
    },
    "references": [
      {
        "title": "Anthropic: Effective context engineering for AI agents",
        "url": "https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents"
      }
    ]
  },
  {
    "id": "agents",
    "part": 1,
    "title": "Supervise the assignment as well as the answer.",
    "nav": "Supervise AI agents",
    "desc": "An AI agent can work through several actions before returning a result. Decide what it may do, what evidence it must preserve, and where the work must come back to a person.",
    "sources": [
      [
        "fall",
        "pp. 10–11"
      ],
      [
        "student",
        "p. 8"
      ]
    ],
    "sections": [
      {
        "h": "Give the system only the authority the assignment needs.",
        "html": "<p>An agent might search approved documents, compare what it finds, and prepare a draft without asking you to start each step. That can be useful when the sequence is clear. It also means that important choices may occur before you see the final page.</p>\n<p>In the vendor matter, reading correspondence is different from contacting the vendor. Preparing a recommendation is different from emailing it to the client. Decide which actions belong in the assignment and which require separate approval. Access should follow that decision rather than expand to include every feature the product offers.</p>\n<p>Also decide what you need to inspect along the way. A polished recommendation may conceal an unsupported date used several steps earlier. Requiring a source-linked timeline before the comparison gives you a place to find that problem while it is still easy to correct.</p>\n"
      },
      {
        "h": "A work order makes the delegated decisions visible.",
        "html": "<p>Before launching an agent, write the assignment as though you were delegating to someone who has no matter context unless you provide it. An <strong>agent work order</strong> makes that assignment explicit. Its twelve parts distinguish what the work should achieve from what the system may do to achieve it.</p>\n<dl class=\"gf-workorder\"><dt>1. Client outcome</dt><dd>State the practical decision or result the client needs. This is the work order’s client outcome.</dd><dt>2. Assignment and scope</dt><dd>Define the assignment and what falls outside it. Avoid granting a broad goal without a manageable scope.</dd><dt>3. Inputs and trusted sources</dt><dd>Name the approved documents or collections and their relevant versions. Identify material it must not rely on.</dd><dt>4. Tools and permissions</dt><dd>Distinguish reading a document or preparing a draft from contacting someone or sending it. Grant only the access this assignment needs.</dd><dt>5. Deliverable</dt><dd>Describe the intended reader and the useful format and level of detail. For example, request a comparison table before a recommendation.</dd><dt>6. Quality standard</dt><dd>Describe an observable standard. A complete comparison, for example, should address every identified requirement without assuming missing facts.</dd><dt>7. Evidence requirement</dt><dd>Specify the source locations or other evidence that will let you inspect important findings. Do not rely on a general assurance that sources were checked.</dd><dt>8. Prohibited behavior</dt><dd>State explicit prohibitions, such as inventing a missing fact or disclosing information outside the approved setting.</dd><dt>9. Escalation triggers</dt><dd>Identify the missing information or conflict that should stop the work. Name the question it should return to you.</dd><dt>10. Human approval points</dt><dd>Identify the reviewer and what cannot proceed without approval. Implement the restriction in the actual software where needed.</dd><dt>11. Test set</dt><dd>Include representative assignments and known failure cases. Describe what the system should do when it cannot complete the task.</dd><dt>12. Record and version</dt><dd>Identify which instructions, results, and approvals should be retained, where they belong, and who maintains the current version.</dd></dl><p class=\"gf-source-caption\">Source: The AI-Enabled Lawyer, p. 11. The labels retain the source framework; the explanations adapt it for this guide.</p>\n\n<p>Notice the distinctions. The client outcome explains the decision the work should support. The deliverable describes what you need back. A quality standard describes how you will judge that result; an evidence requirement says what support must accompany it. Prohibited behavior identifies limits, while escalation triggers identify questions that need someone else's decision.</p>\n<p>Human approval points also differ from tests. Approval is a decision in the actual assignment. A test asks how the proposed workflow behaves on an example before you rely on it. Keeping these subjects separate makes it easier to discover what a seemingly complete instruction has left unanswered.</p>\n<p>The following excerpt shows those choices applied to the fictional vendor assignment. It is a prepared example, not an approved work order for a live matter:</p>\n<div class=\"gf-example\" data-reading-example=\"true\"><header><h3>A worked assignment for the fictional vendor matter</h3></header><div class=\"gf-example-body\"><div class=\"gf-option\"><h4>Client outcome</h4><p>Help the client decide what must be established or done before terminating a software vendor for reported service failures.</p></div><div class=\"gf-option\"><h4>Assignment and scope</h4><p>Identify the relevant contractual requirements and compare them with the supplied factual record. Prepare an internal recommendation only after the lawyer reviews the comparison. Do not conduct new legal research or contact anyone.</p></div><div class=\"gf-option\"><h4>Inputs and trusted sources</h4><p>Use the signed agreement, the supplied amendment, service records, correspondence, and the lawyer’s governing-law analysis. Keep the source locations for each material finding.</p></div><div class=\"gf-option\"><h4>Tools and permissions</h4><p>Read and compare the approved documents. Prepare tables and a draft for the lawyer. Do not send messages, share the source material elsewhere, or change any external records.</p></div><div class=\"gf-option\"><h4>Deliverable</h4><p>First provide separate requirements and timeline tables. Then compare the reviewed findings. After approval, prepare a one-page internal recommendation that preserves unresolved questions.</p></div><div class=\"gf-option\"><h4>Quality standard</h4><p>Address each relevant requirement and distinguish established evidence from allegations. Do not treat a sent notice as proof of receipt. The lawyer must be able to trace every material conclusion to the provided support.</p></div><div class=\"gf-option\"><h4>Evidence requirement</h4><p>Cite the contract provision and record location for each material finding. Identify contrary evidence and information that the packet does not establish.</p></div><div class=\"gf-option\"><h4>Prohibited behavior</h4><p>Do not invent dates or missing documents. Do not assume that termination is permitted merely because a receipt date is established. Do not contact the client or vendor.</p></div><div class=\"gf-option\"><h4>Escalation triggers</h4><p>Stop before a complete recommendation if receipt evidence or another material requirement is unresolved. Return the missing information to the lawyer and ask how to proceed.</p></div><div class=\"gf-option\"><h4>Human approval points</h4><p>The reviewing lawyer approves the comparison and the approach before drafting. The lawyer then reviews the draft before any external use. Adding a document does not count as approval.</p></div><div class=\"gf-option\"><h4>Test set</h4><p>Test the plan with receipt evidence missing, supplied, and conflicting. Confirm that a missing amendment is reported and that a request to send the recommendation is not acted on without approval.</p></div><div class=\"gf-option\"><h4>Record and version</h4><p>Save the approved assignment, source versions, reviewed findings, decisions, and draft in the authorized matter workspace. The supervising lawyer maintains the current record.</p></div></div><p class=\"gf-source-caption\">Prepared example developed for the workflow guide. It does not configure a tool or authorize a live use.</p></div>\n\n<p>Writing these instructions does not configure the application's permissions. A request not to send a message and a technical restriction that prevents sending are different protections. Implement and test the necessary controls in the authorized tool. The optional worksheet offers a place to draft the same assignment; the substantive questions are all above.</p>\n"
      },
      {
        "h": "Look for the error that made the final answer possible.",
        "html": "<p>When a result goes wrong, work backward. Did the system misunderstand the goal? Did a source go missing? Did an allegation become an accepted fact? An early mistake can supply the premise for several later steps, so editing the last paragraph may leave the cause untouched.</p>\n<p>Consider an agent asked to recommend the fastest way to resolve a dispute. It may produce an answer that favors speed while overlooking the client's need to preserve a commercial relationship. The problem began in the objective. Another agent may accurately compare the sources it retrieved but omit the amendment that changes the result. That problem began in the source collection or retrieval step.</p>\n<p>Use the workflow to decide where the issue should have surfaced. A required source list can reveal a missing amendment. A lawyer's review of the proposed objective can expose the tradeoff hidden in “fastest.” The useful control addresses the particular failure rather than adding a general demand for accuracy to every prompt.</p>\n\n<p>Watch for six recurring management failures. A <strong>wrong objective</strong> substitutes a convenient measure for the client's actual result. <strong>Cascading error</strong> turns an early mistake into the premise of later work. A <strong>hidden omission</strong> leaves out a source, issue, or affected person while producing complete-looking prose. <strong>Permission creep</strong> gives the agent more access or authority than the task requires. <strong>Self-confirmation</strong> treats another model response as independent support. <strong>Silent uncertainty</strong> turns a missing answer into a guess instead of returning it for a decision.</p>\n<p>Each failure suggests a different intervention. Reviewing the objective will not find a missing amendment unless the source review also checks completeness. A stricter source requirement will not prevent an unauthorized email unless the system's action permissions address sending. Use the failure to select the control rather than demanding more caution in general.</p>\n"
      },
      {
        "h": "Test whether the software enforces the important limits.",
        "html": "<p>A written prohibition tells the system what you expect. A technical restriction limits what it can do. For consequential actions, find out which protection the application provides and how it behaves when approval is missing.</p>\n<p>Test the boundary with a safe example. Ask the system to prepare an internal comparison, then introduce a request to send it externally. Does sending remain blocked? If a retrieved document contains instructions to ignore the assignment or reveal unrelated information, are those instructions treated as untrusted source content? This problem is called <strong>prompt injection</strong>. It is a reason to limit permissions and test the system, not merely add a warning to the prompt.</p>\n<p>Keep the route back to a person explicit. Name who reviews the question, what information they receive, and what authorization is needed to continue. An agent's statement that it is confident cannot substitute for a decision the assignment reserves to a lawyer.</p>\n"
      },
      {
        "h": "Include examples where stopping is the correct result.",
        "html": "<p>A useful test has an expected outcome. With a missing amendment, the system should identify the gap and avoid claiming a complete review of the contract. With conflicting dates, it should preserve the conflict and ask for the specified decision. With an unapproved external action, it should stop before taking it.</p>\n<p>Test ordinary assignments as well. A system that refuses everything would avoid some errors while failing to do the work. You need evidence that it completes the intended tasks and handles their limits appropriately. Keep representative examples and known failures so you can rerun them after changing instructions, sources, or the underlying product.</p>\n<p>Record what happened, including failures and the review they required. That record helps you decide whether to revise the workflow, narrow its use, or stop using it for the task. The <a href=\"#/lab/shipping\">testing worksheet</a> gives you a place to organize the evidence and remaining questions.</p>\n\n<p>Management continues after a successful test. Keep the records that the risk and assignment warrant, examine recurring failures, and update instructions when the law, sources, or system change. A workflow that repeatedly misses its standard may need a narrower job or retirement. This is part of managing the service, not a verdict on whether AI in general is useful.</p>\n"
      }
    ],
    "quiz": {
      "q": "An agent asks to email the client while preparing an internal comparison. What should you consider first?",
      "a": [
        "Whether the agent can draft the email in the firm’s usual style.",
        "Whether sending an email is necessary and authorized for the assignment.",
        "Whether email access would let it finish the internal comparison sooner."
      ],
      "correct": 1,
      "why": "Permission should follow the defined task. Preparing an internal comparison does not by itself justify access to external communication, even when that access would be convenient."
    },
    "references": [
      {
        "title": "Anthropic: Building effective agents",
        "url": "https://www.anthropic.com/engineering/building-effective-agents"
      }
    ]
  },
  {
    "id": "writing",
    "part": 1,
    "title": "Make the writing clearer without changing what it says.",
    "nav": "Improve legal writing",
    "desc": "Learn how to direct and evaluate a revision through complete worked examples, from a fee-table sentence to a client recommendation. The writing choices and their consequences are visible before any optional practice.",
    "sources": [
      [
        "slides",
        "pp. 20–24, 40–57, 78–87"
      ]
    ],
    "sections": [
      {
        "h": "Diagnose what the reader needs before requesting a rewrite.",
        "html": "<p>“Make this clearer” leaves the most important writing choices unstated. Does the opening delay the answer? Does the sentence hide who acted? Does the analysis state a rule without connecting the facts to it? A useful revision begins with a diagnosis of the reader's problem.</p>\n<p>That diagnosis also tells you which kind of assistance to seek. <strong>Rewriting</strong> can explore a heading, opening, or sentence whose emphasis and style deserve attention. <strong>Editing</strong> can identify confusing, cluttered, or dense passages without replacing them. <strong>Drafting</strong> can turn supplied substance into an email or other defined document when you understand the result well enough to judge it. A request to <strong>summarize or organize</strong> can make a collection of information easier to examine. <strong>Analysis</strong> can explore issues, themes, supporting arguments, and objections after your own first pass.</p>\n<p>These tasks can recur throughout a matter. After gathering authorities, you might ask for several ways to organize their relevant propositions. After selecting a rule, you might ask which distinctions the proposed synthesis leaves unresolved. After writing, you might seek a diagnosis of where a reader needs another explanatory step. The workshop emphasizes small, useful contributions within the work rather than giving AI the whole task at once.</p>\n<p>The examples below show how this looks in writing. Each includes the relevant passage and explanation. You can read the comparisons directly or try the separate exercise before returning; the teaching does not depend on submitting an answer.</p>\n"
      },
      {
        "h": "A more specific request gives you a more useful comparison.",
        "html": "<p>The fee-table example begins with a sentence that describes the table's intended purpose rather than what it does for the reader:</p>\n<div class=\"gf-example\" data-reading-example=\"true\"><header><h3>Original sentence</h3></header><div class=\"gf-example-body\"><p>The foregoing Fee Table is intended to assist investors in understanding the costs and expenses that a shareholder in the Fund will bear directly or indirectly.</p></div><p class=\"gf-source-caption\">Source: Leveling Up Your AI Prompting, slides 20.</p></div>\n\n<p>The workshop then compares a general request for clarity, a request for a stronger verb, and more extensive guidance using examples and alternatives:</p>\n<div class=\"gf-example\" data-reading-example=\"true\"><header><h3>Compare the different requests</h3></header><div class=\"gf-example-body\"><div class=\"gf-option\"><h4>A · General clarity request</h4><p>The above Fee Table aims to help investors comprehend the costs and expenses that a shareholder in the Fund will incur, either directly or indirectly.</p><p class=\"gf-explanation\">This version replaces some words but keeps the indirect description of the table’s purpose. Consider whether “aims to help” and “comprehend” make the relationship easier to understand.</p></div><div class=\"gf-option\"><h4>B · Stronger-verb request</h4><p>The Fee Table informs investors of the costs and expenses borne by Fund shareholders.</p><p class=\"gf-explanation\">“Informs” gives the sentence a more direct verb. Read closely, though: the original distinction between costs borne directly and indirectly is no longer explicit. A shorter sentence must still convey the intended information.</p></div><div class=\"gf-option\"><h4>C · Guided alternative</h4><p>The Fee Table above shows investors the costs and expenses a shareholder in the Fund will bear, directly or indirectly.</p><p class=\"gf-explanation\">“Shows” describes what the table does, while the sentence preserves direct and indirect costs. This is one possible revision. Judge whether it fits the surrounding document and its reader.</p></div></div><p class=\"gf-source-caption\">Source: Leveling Up Your AI Prompting, slides 21–24. Commentary developed for this guide.</p></div>\n\n<p>The first response changes words but leaves the indirect construction largely intact. The second gives the sentence a more direct verb, yet no longer expressly distinguishes direct from indirect costs. The guided version uses “shows” while retaining that distinction. The important comparison is therefore not merely length or energy. It is what the reader understands and which meaning survives.</p>\n<p>There are other defensible arrangements. The workshop's later options begin with the costs, frame the sentence as the investor's question, or split the explanation into two sentences. Those alternatives help you decide where to place the reader's attention. They are more informative than a set of synonyms that leaves the same sentence untouched.</p>\n<p>Your own knowledge of sentence craft makes the request better. If you can identify a weak verb, an obscured actor, or an unnecessary description of intention, you can ask the system to address the problem and examine whether it did. A fluent response is not the same thing as a well-directed revision.</p>\n"
      },
      {
        "h": "Teach a writing choice, not a writer's surface mannerisms.",
        "html": "<p>The dog-toy introduction in the workshop demonstrates how a writer can give the reader something concrete to understand before introducing the legal dispute. The original practice passage begins abstractly:</p>\n<div class=\"gf-example\" data-reading-example=\"true\"><header><h3>Original practice introduction</h3></header><div class=\"gf-example-body\"><p>This action arises from the design, marketing, and sale of a dog toy by Respondent VIP Products. The product at issue is a squeaky chew toy that was made to resemble, in certain respects, a bottle of Jack Daniel’s whiskey, including aspects of the bottle’s label, wording, and overall appearance, even though the toy does not copy the Jack Daniel’s product in every detail or exact particular.</p><p>As part of that design, the toy uses the phrase “Bad Spaniels” in place of the words “Jack Daniel’s,” and it also replaces the phrase “Old No. 7 Brand Tennessee Sour Mash Whiskey” with the phrase “The Old No. 2 On Your Tennessee Carpet,” while otherwise retaining a number of features and design elements that are intended to evoke the Jack Daniel’s bottle and the commercial impression associated with it.</p><p>This case concerns the creation, promotion, and sale of that product and the legal issues alleged to result from the similarities between the toy and the Jack Daniel’s bottle and label.</p></div><p class=\"gf-source-caption\">Source: Leveling Up Your AI Prompting, slides 40 and 43.</p></div>\n\n<p>The workshop contrasts that passage with this excerpt from the opinion:</p>\n<div class=\"gf-example\" data-reading-example=\"true\"><header><h3>The opinion excerpt supplied in the workshop</h3></header><div class=\"gf-example-body\"><p>This case is about dog toys and whiskey, two items seldom appearing in the same sentence. Respondent VIP Products makes a squeaky, chewable dog toy designed to look like a bottle of Jack Daniel’s whiskey. Though not entirely. On the toy, for example, the words “Jack Daniel’s” become “Bad Spaniels.” And the descriptive phrase “Old No. 7 Brand Tennessee Sour Mash Whiskey” turns into “The Old No. 2 On Your Tennessee Carpet.”</p></div><p class=\"gf-source-caption\">Source: Leveling Up Your AI Prompting, slides 41; the workshop identifies Justice Elena Kagan’s prose in the following discussion. The excerpt illustrates writing, not a rule for the other examples.</p></div>\n\n<p>The reader first encounters the subject and the company making it. The label changes then explain how the toy evokes the bottle. The concrete details do the explanatory work that phrases such as “design, marketing, and sale” or “commercial impression associated with it” leave to the reader.</p>\n<p>A generic request for clarity may preserve the abstract opening and rearrange the same nouns. Better direction identifies what should change: name the actor, describe the product and conduct, give the reader the label comparisons, and let the legal issue emerge from those facts. A sample can demonstrate the move without supplying facts for a new matter.</p>\n<p>The workshop's extended editing request follows a useful process. Diagnose the original and identify its core point. Develop meaningfully different candidates, evaluate them against stated criteria, select a small set worth examining, and explain which choices changed. A recommendation can then identify the best fit for the purpose. The explanation matters because it lets the writer learn and disagree; an unexplained score is not enough.</p>\n<p>Preserve the ground rules from that example. Do not change an already effective passage merely to appear useful. Flag an ambiguity that requires a substantive decision instead of silently choosing. Keep source facts, quotations, and propositions intact. A brief, an opinion, and a client email may borrow an explanatory technique while requiring different tones. Copying a celebrated writer's fragments or distinctive metaphors is not the same thing as learning how that writer helps the reader.</p>\n"
      },
      {
        "h": "Place an unresolved condition beside the decision it affects.",
        "html": "<p>Stonebridge wants confirmation that it can pay a $12 million dividend. Here is the supplied passage:</p>\n<div class=\"gf-example\" data-reading-example=\"true\"><header><h3>Original Stonebridge passage</h3></header><div class=\"gf-example-body\"><p>With respect to Stonebridge’s request for confirmation concerning its proposed $12 million dividend, which it has asked us to respond to by Friday, we reviewed Section 6.04 and the leverage calculation provided by Stonebridge. Section 6.04 provides that a restricted payment may be made so long as no default exists and the total net leverage ratio, calculated on a pro forma basis, does not exceed 4.75x. No separate default has been identified. Stonebridge’s calculation reflects a leverage ratio of 4.68x, but it should be noted that the calculation includes $3.2 million in projected cost savings. The projected savings are relevant because, if they are excluded, the leverage ratio is 4.93x rather than 4.68x. Although the agreement allows projected cost savings to be included, it also provides that such savings must be reasonably identifiable, factually supportable, and expected to be realized within 18 months. To date, no materials supporting the projected savings have been provided. Therefore, although the dividend may be permitted, we do not currently have enough information to confirm that it is permitted, and additional support should be requested from Stonebridge.</p></div><p class=\"gf-source-caption\">Source: Leveling Up Your AI Prompting, slides 56.</p></div>\n\n<p>The reported ratio is below the contractual ceiling only because it includes projected savings for which supporting material has not been provided. That relationship should be easy to see. A reader should not have to reconstruct it from the order in which the lawyer performed the review.</p>\n<p>Here is a prepared revision from this guide, not an answer supplied in the original slides:</p>\n<div class=\"gf-example\" data-reading-example=\"true\"><header><h3>A prepared revision for comparison</h3></header><div class=\"gf-example-body\"><p>We cannot yet confirm that Stonebridge may pay its proposed $12 million dividend. Before responding by Friday, we should request support for the $3.2 million in projected cost savings included in its leverage calculation.</p><p>Section 6.04 permits a restricted payment if no default exists and the pro forma total net leverage ratio does not exceed 4.75x. No separate default has been identified. Stonebridge reports a ratio of 4.68x with the projected savings, but the ratio would be 4.93x without them.</p><p>The agreement allows projected savings that are reasonably identifiable, factually supportable, and expected to be realized within 18 months. Because Stonebridge has not supplied supporting materials, we cannot yet determine whether the savings satisfy those conditions.</p></div><p class=\"gf-source-caption\">Prepared for this guide from the supplied facts; not an original-source answer key.</p></div>\n\n<p>The revision leads with what can be said now and connects the request for support to the deadline. The ratios then explain why the support matters. It preserves the three conditions for counting projected savings and the difference between “no separate default has been identified” and a finding that no default exists.</p>\n<p>That is substantive editing as well as sentence editing. “The dividend is prohibited” would be more decisive and less faithful to the record. “Additional diligence is needed” would be shorter and less useful to the person who needs to provide the support. The writing should make the present uncertainty and its consequence precise.</p>\n"
      },
      {
        "h": "Explain separate concerns as separate questions.",
        "html": "<p>Falcon Medical's proposed disclosure raises a comparison between confidentiality obligations and a separate question about how much information the recipient needs. The original passage supplies both:</p>\n<div class=\"gf-example\" data-reading-example=\"true\"><header><h3>Original Falcon Medical passage</h3></header><div class=\"gf-example-body\"><p>The issue is whether Falcon Medical’s monthly reporting package can be sent today to Redwood, which is a prospective assignee and has signed our standard NDA. As an initial matter, disclosure of confidential information to a prospective assignee is permitted under Section 9.12 if confidentiality obligations at least as protective as those in Section 9.12 are agreed to by the recipient. Although an NDA has been signed by Redwood, the NDA contains a residuals clause, meaning that information retained in unaided memory may be used. A comparable provision is not included in Section 9.12, under which use is limited to evaluating or acquiring the loan. This difference could mean that the NDA is not as protective. It should also be noted that customer-level revenue, pricing information, and annual forecasts are included in the package, even though Redwood currently needs only summary financial information. In light of the fact that the NDA may not satisfy Section 9.12, consideration should be given either to revising the NDA or removing certain information before the package is sent.</p></div><p class=\"gf-source-caption\">Source: Leveling Up Your AI Prompting, slides 57.</p></div>\n\n<p>A signed NDA is not automatically an NDA that meets Section 9.12. The residuals clause may permit use that the credit agreement does not allow. The excess customer information creates a related concern, but reducing the package does not itself resolve the difference in contractual protections.</p>\n<p>Here is the guide's prepared comparison:</p>\n<div class=\"gf-example\" data-reading-example=\"true\"><header><h3>A prepared revision for comparison</h3></header><div class=\"gf-example-body\"><p>Before sending Falcon Medical’s monthly reporting package to Redwood today, we should resolve whether Redwood’s NDA meets Section 9.12 and review how much information Redwood needs.</p><p>Section 9.12 permits disclosure to a prospective assignee that agrees to confidentiality obligations at least as protective as its own. Although Redwood has signed our standard NDA, the NDA allows use of information retained in unaided memory. Section 9.12 has no comparable provision and limits use to evaluating or acquiring the loan, so the NDA may be less protective.</p><p>The package also contains customer-level revenue, pricing information, and annual forecasts, even though Redwood currently needs only summary financial information. Consider revising the NDA or narrowing the package before sending it. Removing unnecessary detail should not be treated as resolving the separate question of whether the proposed disclosure complies with Section 9.12.</p></div><p class=\"gf-source-caption\">Prepared for this guide from the supplied facts; not an original-source answer key.</p></div>\n\n<p>The first sentence gives the reader two questions to resolve rather than presenting signature of the NDA as the answer. The following paragraphs explain the legal comparison and the unnecessary detail in the package. The conclusion remains conditional: the NDA may be less protective.</p>\n<p>The original passage suggests revising the NDA or removing information. This guide adds the caution that narrowing the package should not be treated as a complete legal cure without examining what would remain and what the agreement permits. That caution is an explanatory addition; the source does not supply a final legal determination. Separating the concerns makes the further analysis visible instead of using a cleaner sentence to hide it.</p>\n"
      },
      {
        "h": "Ask for an explanation you can check against the revision.",
        "html": "<p>A useful editing response should help you learn from the changes. Ask the tool what it moved, what it cut, and which edits might affect meaning. Then compare that account with the actual text. The explanation is another work product to assess; it may miss an important change.</p>\n<div class=\"prompt-box\"><div class=\"prompt-top\"><span>Instructions to adapt</span><button class=\"text-btn\" data-copy-parent=\".prompt-box\">Copy instructions</button></div><pre>Before rewriting, explain what the reader needs to understand and what currently makes that difficult. Preserve the supplied facts, numbers, conditions, and uncertainty. Offer two versions with meaningfully different organization and explain what each emphasizes. Flag any proposed change that could affect the analysis for my decision. Do not add facts or legal conclusions.\n\nAudience and purpose: [describe them].\nPassage: [paste it].</pre></div>\n<p>After you select an approach, read the passage again without the surrounding conversation. Can the intended reader identify the recommendation, understand the reason, and tell what happens next? That is the document's job. The prompt should help you get there, but the final text must work on its own.</p>\n\n<p>Sometimes identification is the better assignment. Ask the tool to locate every sentence where a reader must hold several ideas at once, every transition that leaves the relationship unexplained, or each place the application of a rule is asserted rather than developed. Ask it to point to the words and explain the problem. You can decide what to revise before the draft is changed.</p>\n<p>Other times you need help with tone or technical explanation. Supply the accurate substance and describe what the reader knows. Ask for ways to introduce the unfamiliar idea through a concrete example, while marking any new analogy as an illustration rather than source evidence. The result still has to preserve the distinction or condition the legal analysis depends on.</p>\n"
      }
    ],
    "quiz": {
      "q": "Stonebridge’s ratio is 4.68x with projected savings and 4.93x without them, against a 4.75x limit. No supporting material for the savings has been supplied. What should the revised advice preserve?",
      "a": [
        "The dividend is permitted because the borrower reported a ratio below the limit.",
        "The dividend is prohibited because the ratio exceeds the limit without the savings.",
        "The current record does not establish whether the savings qualify, so permission cannot yet be confirmed."
      ],
      "correct": 2,
      "why": "The exercise leaves a material question open. A revision can make that question easier to understand, but it cannot resolve it by making the prose more decisive."
    },
    "references": [
      {
        "title": "Write.law: Level up your law",
        "url": "https://write.law/blog/level-up-your-law"
      },
      {
        "title": "Write.law: The power of words",
        "url": "https://write.law/blog/power-of-words"
      }
    ]
  },
  {
    "id": "aiisms",
    "part": 1,
    "title": "Edit the habits that make writing feel generic.",
    "nav": "Remove generic writing",
    "desc": "A passage can use ordinary words and still leave the reader with little to work with. Look at how the writing develops the point, not just whether it contains a familiar AI phrase.",
    "sources": [
      [
        "slides",
        "pp. 58–77"
      ]
    ],
    "sections": [
      {
        "h": "Ask what a phrase contributes to the reader.",
        "html": "<p>When a draft says an issue is “crucial” or “multifaceted,” ask what the reader learns from the description. Often, the useful information comes next: a deadline may expire, a provision may prohibit the proposed disclosure, or an assumption may change the calculation. Give the reader that information instead of announcing its importance.</p>\n<p>The same test applies to transitions. “Moreover” can be perfectly useful, but inserting it before every new point does not explain how the points relate. Does the next sentence add support, qualify a rule, or answer a concern raised by the previous sentence? Write the relationship the reader needs.</p>\n<p>I use <strong>AI-isms</strong> as a name for recurring habits that can make assisted writing feel generic or mechanical. It is an editing category, not a way to establish authorship. Humans use these habits too. Your reason for revising should be what the passage does to the reader.</p>\n\n<p>The source describes two complementary approaches: give clearer directions before drafting, and learn to recognize the patterns during editing. A drafting request might ask the system to introduce the answer promptly, vary sentence and paragraph length according to the material, avoid inflated business language, and develop the relationship among ideas. It should not replace one compulsory rhythm with another.</p>\n"
      },
      {
        "h": "Read at the level of words, sentences, structure, and substance.",
        "html": "<p>At the word level, look for inflated language where a familiar, specific term would do. “Facilitate the implementation of” may hide the action the reader needs to understand. But do not turn a style preference into a ban on technical language. “Leverage” has a precise meaning in the Stonebridge exercise; replacing it indiscriminately would make the analysis worse.</p>\n<p>At the sentence level, notice repeated shapes. A succession of artificial contrasts or equally sized lists can make different ideas sound as though they have the same relationship. Repeated hedges can also obscure the actual uncertainty. Explain what is unresolved instead of stacking “may,” “potentially,” and “possibly.”</p>\n<p>Then stand back from the page. Does every issue receive the same space even though one drives the recommendation? Are headings interrupting an explanation that belongs together? Use paragraphs and lists according to the work they do. A list of required documents may be helpful; a chain of reasoning often needs connected prose.</p>\n<p>Finally, examine the substance. A paragraph may state the law accurately yet never apply it. A recommendation may identify several risks without explaining which one matters to the client. No amount of sentence polishing supplies that missing work.</p>\n"
      },
      {
        "h": "A plain paragraph can still have no useful analysis.",
        "html": "<p>The workshop uses this deliberately weak paragraph to show why the edit must reach beyond words:</p>\n<div class=\"gf-example\" data-reading-example=\"true\"><header><h3>A deliberately weak passage</h3></header><div class=\"gf-example-body\"><p>In today’s rapidly evolving employment landscape, it is crucial to underscore that Ms. Chen’s pre-termination download presents a multifaceted challenge. Her conduct is not merely suspicious—it may potentially support a trade-secret claim. Moreover, the downloaded materials included customer lists, pricing models, and strategic forecasts, all of which could be considered highly sensitive. Furthermore, courts have reached varying conclusions regarding when downloading information becomes threatened misappropriation. Importantly, the company also faces meaningful business, reputational, and litigation risks if it moves too aggressively. Ultimately, we recommend a holistic and measured approach that leverages the existing record while proactively addressing these pivotal concerns. The company should carefully consider its options before deciding whether to seek immediate relief.</p></div><p class=\"gf-source-caption\">Source: Leveling Up Your AI Prompting, slides 67 and 72. The diagnosis below is prepared commentary, not an authorship determination.</p></div>\n\n<p>At the word level, phrases such as “crucial to underscore” and “multifaceted challenge” announce importance without explaining it. At the sentence level, the repeated transitions and the “not merely” contrast supply a rhythm instead of a developed relationship among the ideas. The hedges describe uncertainty without identifying what remains unresolved.</p>\n<p>The larger problem is substantive. The paragraph does not identify the controlling authority, connect a particular fact to a legal requirement, rank the competing concerns, or propose a next action the client can use. Removing the conspicuous language would leave those omissions untouched. A recommendation to “carefully consider its options” offers no basis for choosing among them.</p>\n<p>The appropriate edit therefore depends on the available sources. The paragraph's label for the conduct may itself go beyond the record. Before drafting a more definite recommendation, identify what the law requires, what the evidence establishes, and what the client needs to decide. Where those materials are absent, say what must be obtained rather than inventing a more concrete answer.</p>\n<p>Some of the workshop's contrast passages make this point from the other direction. Ordinary legal writing can contain a contrast, a long sentence, or the word “moreover” and still perform useful analytical work. A plain-sounding recommendation can remain generic because it never applies the rule or weighs the facts. The habits are prompts for inspection, not proof of authorship or automatic reasons to delete a sentence.</p>\n"
      },
      {
        "h": "Do not invent the detail the paragraph is missing.",
        "html": "<p>A vague sentence can tempt us to make the revision more concrete by supplying a fact the source never established. That is especially dangerous when the missing detail is the controlling rule, a deadline, or an enforcement example. The stronger-sounding sentence may be less accurate than the weak one it replaced.</p>\n<p>Suppose a draft says “the data-retention policy presents concerns.” Before making that conclusion specific, you need the applicable requirement and the facts about the policy. You cannot improve it by inventing a universal retention limit. The honest revision identifies the unanswered question and the information needed to resolve it.</p>\n<p>Our Stonebridge and Falcon exercises supply the relevant conditions so you can practice substantive editing within a defined record. In your own work, keep the same discipline: distinguish a writing problem from a gap in the underlying analysis. Sometimes the next step is another sentence. Sometimes it is more research or a question for the client.</p>\n"
      },
      {
        "h": "Teach the system choices from your own writing.",
        "html": "<p>Choose a few approved samples you like and read them for specific decisions. Where do you put the answer? How do you introduce an unfamiliar legal concept? Which details help the reader picture the dispute? Notice the exceptions as well as the patterns, because a brief and a client email may need different treatment.</p>\n<p>Ask AI to help describe those choices, then challenge its account. “Your style is clear and compelling” gives you nothing to reuse. A description of how your openings identify the disputed conduct, or how your paragraphs connect a rule to concrete facts, gives you something you can test.</p>\n<div class=\"prompt-box\"><div class=\"prompt-top\"><span>Instructions to adapt</span><button class=\"text-btn\" data-copy-parent=\".prompt-box\">Copy instructions</button></div><pre>Read these approved writing samples and describe the specific choices that help the reader. Use short examples to support your observations. Explain how the openings, headings, sentences, and paragraphs do their work. Identify exceptions and differences among audiences rather than imposing a fixed rhythm. Avoid general praise. Do not rewrite the samples yet; I will review your description first.</pre></div>\n<p>Save the description once it is accurate enough to guide another assignment. Pair it with examples that show what you mean. Then continue to edit the output yourself. A style description can help the system make better choices, but the choices still need to fit the passage in front of you.</p>\n\n<p>A useful style description also distinguishes your habits from your team's requirements. The workshop asks about full-sentence headings, paragraph length, where the answer appears, contractions, first-person usage, numbered points, and what the first sentence normally does. For a group, the relevant choices may include memo format, defined terms, citation placement, phrases reviewers regularly remove, or vocabulary the group avoids.</p>\n<p>Use approved samples to describe those decisions, then challenge an answer that merely flatters. Push until it says something specific enough to correct. Save the reviewed description with the examples and adapt it to the audience. The numerical “voice vector” and fixed rhythm in one slide are illustrative prompt variables, not required rules for this guide or a universal account of my voice. Here, the material should govern the rhythm, and complete explanations matter more than matching a sentence-length target.</p>\n"
      }
    ],
    "quiz": {
      "q": "A draft uses ordinary words but describes several risks without explaining their importance to this client. What needs attention?",
      "a": [
        "Replace the remaining formal words with shorter ones.",
        "Explain how the relevant facts and rules bear on the client’s decision.",
        "Vary the paragraph lengths so the discussion feels less repetitive."
      ],
      "correct": 1,
      "why": "Changes in wording or paragraph length will not supply the missing analysis. The reader needs to understand what the risks mean in this matter and why a proposed response makes sense."
    },
    "references": [
      {
        "title": "Write.law: The quest to take legal writing from art to science",
        "url": "https://write.law/blog/the-quest-to-take-legal-writing-from-art-to-science"
      }
    ]
  },
  {
    "id": "process",
    "part": 2,
    "title": "Improve the process before adding more technology.",
    "nav": "Improve a process",
    "desc": "Begin with the experience of the person receiving the service. Find out where the work becomes slow, confusing, or unreliable, then decide whether AI would improve it.",
    "sources": [
      [
        "fall",
        "pp. 12–13"
      ]
    ],
    "sections": [
      {
        "h": "Define the result from the client's perspective.",
        "html": "<p>A team can produce an excellent document and still make the service difficult to use. An intake form may ask for the same information twice. A client may receive a carefully drafted explanation but remain unsure what to send next. A request may sit unanswered because no one knows who is responsible for the follow-up.</p>\n<p>Before choosing a tool, describe what should be different when the service works well. For an intake process, that might mean the client understands what information is needed and the reviewing lawyer receives it in a usable form. “Generate a summary” describes one task; it does not establish that broader result.</p>\n<p>Include the people who handle the work between the obvious legal steps. An assistant may know why forms come back incomplete. A client may reveal that a question you considered straightforward is hard to answer. Their experience helps you identify what to change before automating the current process.</p>\n"
      },
      {
        "h": "Examine each part of the service before choosing the technology.",
        "html": "<p>I use nine stages to examine a proposed process improvement. They begin with the client and end with a tested revision, so the choice of a product follows an understanding of the service.</p>\n<h3>Define the outcome and map the current work.</h3>\n<p>State the change that should happen for the client: a decision made, a dispute resolved, a right exercised, a risk reduced, or a burden removed. Then describe how the service currently reaches that result. Include the client, staff, lawyers, courts, vendors, and systems where they play a role. Show the inputs, handoffs, waiting, decisions, and repeated work, not only the legal drafting steps.</p>\n<h3>Find friction and failure, then remove before adding.</h3>\n<p>Look for duplicated requests, unclear responsibility, information gaps, inconsistent judgment, and places where errors remain hidden. Ask whether each step protects something valuable. Remove a step that contributes nothing; standardize work that ought to be consistent. A simpler instruction or clearer assignment may solve the problem before AI becomes necessary.</p>\n<h3>Assign the best actor and build the controls.</h3>\n<p>Decide which work belongs to the client, a lawyer, a staff member, an AI tool, an agent, or an outside expert. Pair the assignment with the source requirements, permissions, approvals, and stopping conditions that address its risk. This includes deciding where a lawyer must weigh competing values rather than merely complete a checklist.</p>\n<h3>Pilot narrowly and measure the whole result.</h3>\n<p>Test a limited use with representative users and examples near the boundaries. Observe quality, time, cost, correction work, client effort, accessibility, equity, and learning. A faster first draft is not enough evidence if the reviewer needs more time to repair it or the client needs more help to understand it.</p>\n<h3>Revise and version.</h3>\n<p>Examine what happened, record the change, and test again. The source treats failure and feedback as information for the next version. A process that cannot meet its standard should not continue merely because the team has invested effort in it.</p>\n<p>These paragraphs follow the source's nine stages: define, map, find, remove, assign, control, pilot, measure, and revise. They are an investigation of the service, not a claim that filling out nine fields proves the redesign works.</p>\n"
      },
      {
        "h": "A process map can reveal a problem another memo would miss.",
        "html": "<p>Consider a fictional intake process. The client enters information in a form, an assistant retypes it into a summary, a lawyer asks follow-up questions, and the client supplies information that could have been requested at the outset. Drafting the summary faster addresses only one step. It does not resolve the duplicate entry or the unclear question that caused the follow-up.</p>\n<p>A useful map identifies the people involved, what each needs from the preceding step, and where a decision must be made. Perhaps the assistant should receive structured information directly. Perhaps a plain-language explanation belongs beside a confusing question. Perhaps a lawyer needs to speak with the client before the remaining form can sensibly be completed. Those are different improvements, and only some may benefit from AI.</p>\n<p>Several further questions help examine the proposed service. Who is trying to accomplish what, and where does the current service impose confusion, effort, delay, or exclusion? What should change in the world? Which steps protect value and which persist by tradition? Where must a lawyer weigh uncertainty and consequences? What control protects each risky step? How will failures, feedback, and changed law improve the next version?</p>\n<p>The map is an analytical tool, not proof that the service is safe or useful. It gives the people responsible for the work something concrete to question. The optional process worksheet records the same inquiry for a service you bring.</p>\n"
      },
      {
        "h": "Measure the work that happens after the draft appears.",
        "html": "<p>A faster first draft may shift work to the reviewer. A shorter form may produce more follow-up questions. To judge the proposed process, include those consequences in the comparison.</p>\n<p>For a document-summary task, record meaningful errors and the time needed to check and repair them. For intake, consider how often information is missing and where users need help. Where the change affects access, learning, or the distribution of work, examine those effects too. The measures should fit the service you are trying to improve.</p>\n<p>For an organization managing several AI uses, NIST's AI Risk Management Framework and its Generative AI Profile provide a broader reference. They address responsibility, context, measurement, and response to risk. The framework is a voluntary resource, not a certification conferred by completing this worksheet. Use the linked source notes to explore it when the organizational question calls for more detail.</p>\n\n<p>NIST's framework uses the terms <strong>govern</strong>, <strong>map</strong>, <strong>measure</strong>, and <strong>manage</strong>. The source applies them as an organizational perspective: identify ownership, understand the context and affected people, examine performance and risk, and decide how to respond and improve. That larger perspective helps connect an individual workflow with responsibility for the service as a whole.</p>\n"
      },
      {
        "h": "Try the revised process with someone who has not helped design it.",
        "html": "<p>Consider a fictional clinic or firm intake process. Choose one instruction that people are likely to misunderstand. Rewrite it, explain what information or protection the revised version must preserve, and ask someone else to use it without your coaching.</p>\n<p>Watch where they hesitate. Do they know what the question is asking? Can they find what happens next? A lawyer might test with a colleague or a representative user; students can begin with classmates using fictional facts. In either setting, avoid using a live client service as an unsupervised experiment.</p>\n<p>Compare what happened with what you expected. You may discover that the main problem was the order of the questions rather than their wording, or that the process needs a person available at a particular point. Record that finding before deciding whether an AI feature would help. The test should improve your understanding of the service as well as the proposed tool.</p>\n"
      }
    ],
    "quiz": {
      "q": "A team wants to automate a recurring legal service. Where should its review begin?",
      "a": [
        "With the client’s need and how the current service tries to meet it.",
        "With a comparison of the available automation products.",
        "With a plan to reproduce the current steps more quickly."
      ],
      "correct": 0,
      "why": "Understanding the service may reveal that some steps should change or disappear. Choosing a tool before examining the work can preserve problems that technology was supposed to solve."
    },
    "references": [
      {
        "title": "NIST AI Risk Management Framework",
        "url": "https://www.nist.gov/itl/ai-risk-management-framework"
      }
    ]
  },
  {
    "id": "building",
    "part": 2,
    "title": "Build a small version and test what it does.",
    "nav": "Build and test a tool",
    "desc": "AI-assisted coding can help you explore a useful tool by describing its behavior. Your contribution begins with the problem, the requirements, and the tests that would reveal whether the idea works.",
    "sources": [
      [
        "fall",
        "p. 15"
      ]
    ],
    "sections": [
      {
        "h": "Treat the first version as a proposal to investigate.",
        "html": "<p>Suppose your team repeatedly checks whether a document contains specified notice provisions. You might describe a tool that asks for those provisions and organizes them for a lawyer's review. A working prototype would let you examine whether that interface helps with the task.</p>\n<p>It would not establish that the tool correctly understands every agreement, protects uploaded files, or is ready for clients to use. Those are separate questions that need evidence. A demonstration usually shows a selected example under selected conditions.</p>\n<p>You may hear the term <strong>vibe coding</strong> for building through natural-language instructions and AI-generated code. For our purposes, the useful skill is translating a legal or practical need into behavior someone can observe and test. Start with fictional data and a limited purpose. Bring in appropriate technical expertise before another person depends on a system whose security or reliability you cannot assess.</p>\n"
      },
      {
        "h": "Describe the behavior instead of naming an impressive feature.",
        "html": "<p>“Build a legal assistant” leaves most of the important decisions open. “Build a form that records the notice provision, flags a missing receipt date, and prepares a checklist for lawyer review” gives the builder something more definite to implement.</p>\n<p>For each important feature, describe what the user supplies and what should happen. In the vendor example, what does the tool do when a date is missing? Does it distinguish sending from receipt? Can the user inspect the source supporting a result? Does the interface make an unresolved question look like a completed review?</p>\n<p>Also describe what the tool must not do. A prototype for organizing notice information should not silently become a deadline calculator or an individualized recommendation to terminate. Legal rules often include conditions and exceptions that a neat interface can hide. Keep the proposed scope narrow enough that you can explain and test those boundaries.</p>\n\n<p>The source places the lawyer's contribution in problem selection, requirements, legal logic, test design, user experience, and governance. That is a practical way to collaborate with a technical specialist: bring a recurring problem worth solving, explain the rule and exceptions, identify the consequences of failure, and describe behavior you can test. The collaboration gives your legal knowledge a more direct role in building the service.</p>\n"
      },
      {
        "h": "Six questions separate a prototype from a responsible pilot.",
        "html": "<p>A prototype shows that an idea can be explored. It does not establish that the tool is accurate, secure, maintained, legally compliant, or ready for public use. Before someone depends on the tool, the team should be able to explain six areas of the proposed use.</p>\n<p><strong>User validation</strong> asks whether representative users have tried the tool and what the team observed. Confusion, workarounds, inaccessible features, and unexpected needs are evidence about the design. A successful demonstration by its creator answers a different question.</p>\n<p><strong>Legal logic and sources</strong> asks whether the relevant rules are current, jurisdiction-specific, traceable, and within the proposed scope. The tool should distinguish authority from inference and general information from advice. A legal rule may also include exceptions or judgment that cannot responsibly be hidden behind a yes-or-no result.</p>\n<p><strong>Failure behavior</strong> asks what happens with missing facts, conflicting sources, ambiguity, instructions trying to redirect the system, and requests outside scope. A test should state the expected behavior before it runs. Sometimes the correct result is to stop and ask a lawyer.</p>\n<p><strong>Data and security</strong> concerns the authorized environment and the permissions, retention, logging, access, and inputs the task actually needs. A working interface does not answer these questions. The relevant technical and organizational review still has to occur.</p>\n<p><strong>The human path</strong> asks whether users can reach an accountable person and whether that person handles consequential decisions, exceptions, individualized judgment, and external actions. A disclaimer is not a substitute for the route to help that the service requires.</p>\n<p><strong>Ownership and maintenance</strong> asks who watches performance, updates sources, approves changes, rolls back a bad version, and retires the system. The service needs that responsibility after launch as well as before it.</p>\n<p>The optional review worksheet records the evidence behind these questions. Its checkmarks do not verify the evidence or certify readiness. The standard is the team's ability to explain the use and demonstrate the relevant behavior.</p>\n"
      },
      {
        "h": "Write down what a test should show.",
        "html": "<p>A test is more useful when you decide the expected behavior before running it. For a missing receipt date, you may expect a visible warning and no calculated cure-period conclusion. For conflicting documents, you may expect the tool to show the conflict and route it to a lawyer. For an ordinary complete example, you should expect it to perform the intended task without unnecessary refusal.</p>\n<p>Include cases near the boundaries of the tool's scope and examples of failures you have already seen. Repeat important tests after a change. A clearer instruction or a new model can improve one result while creating another problem.</p>\n<p>Test the experience as well as the answer. Ask someone who did not build the tool to use it without explanation. Can they find the source, understand the limitation, and tell what they should do next? A technically correct response can still mislead if the interface presents it as more conclusive than it is.</p>\n"
      },
      {
        "h": "Decide who will keep the tool fit for use.",
        "html": "<p>Before a pilot begins, identify who can approve a change, investigate a failure, and withdraw a version that no longer works as intended. Someone also needs to watch for changes in the relevant law, sources, and software.</p>\n<p>Make the user's route to a person understandable. A warning that says “consult a lawyer” may be inadequate if the service gives the user no practical way to do so. Where the workflow reserves a consequential decision for human review, that review needs to happen before the action, not after it.</p>\n<p>Keep the first release limited to the purpose and evidence you can support. You can expand later when testing gives you a basis for it. A useful prototype is a way to learn about the problem and the proposed solution; preparing it for dependable use is further work that needs an owner.</p>\n"
      }
    ],
    "quiz": {
      "q": "A prototype works well in a demonstration. What can the team reasonably conclude?",
      "a": [
        "The demonstration establishes that users can rely on its legal answers.",
        "The idea is ready to examine further, but its accuracy, failure behavior, and suitability still need review.",
        "The rules will stay accurate as long as the interface is unchanged."
      ],
      "correct": 1,
      "why": "A demonstration shows a particular result under particular conditions. Before other people depend on the tool, the team needs to test a broader range of cases and decide who will maintain it."
    },
    "references": [
      {
        "title": "NIST Generative AI Profile",
        "url": "https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence"
      }
    ]
  },
  {
    "id": "playbook",
    "part": 3,
    "title": "Keep a record that improves the next assignment.",
    "nav": "Keep what you learn",
    "desc": "A successful prompt is easier to reuse when you know why it worked. Save the task, the necessary materials, and what you learned from checking the result.",
    "sources": [
      [
        "fall",
        "p. 16"
      ],
      [
        "slides",
        "pp. 35, 74–77"
      ],
      [
        "short",
        "pp. 1–2"
      ]
    ],
    "sections": [
      {
        "h": "Save the reason the method was useful.",
        "html": "<p>A folder of prompts can grow quickly without becoming much help. Months later, you may remember that a request produced an excellent answer but not what information you supplied, what you corrected, or when the same request would be inappropriate.</p>\n<p>Begin with one example worth keeping. Describe the assignment and the contribution AI made. Preserve enough of the instructions and result to show what worked, subject to the rules for retaining and sharing the material. Add a note about the checks and limitations.</p>\n<p>For example, a heading prompt may be useful because it asks for alternatives that begin with different facts. Record that purpose. Another lawyer can then decide whether the technique fits a new document rather than copying the request and hoping for the same effect.</p>\n"
      },
      {
        "h": "Record enough for another lawyer to understand the method.",
        "html": "<p>A useful playbook has six parts, each serving a different purpose. <strong>Principles</strong> explain what AI should help expand and which judgments you intend to protect. <strong>When-not-to-use rules</strong> identify uses that are prohibited, unsafe, harmful to learning, or more expensive to verify than to do yourself. A <strong>prompt and harness library</strong> keeps reusable instructions with the source requirements and examples behind them.</p>\n<p><strong>Workflow and process</strong> shows where assistance belongs in the assignment and where human decisions occur. <strong>Failures</strong> records hallucination, omission, overbreadth, bias, narrowed thinking, or implementation problems and examines why they happened. A <strong>personal development plan</strong> identifies the legal and managerial skills you will practice independently, with AI assistance, and as a supervisor of AI-enabled work.</p>\n<p>A useful entry is specific enough to apply and limited enough not to invite careless reuse. Here is a prepared example:</p>\n<blockquote>\n<p><strong>Method:</strong> Compare alternative openings for an advice paragraph after determining what the record supports.<br />\n<strong>What helped:</strong> Asking one version to foreground the unresolved condition and another to foreground the information the client needs to supply made the choice of emphasis visible.<br />\n<strong>What I rejected:</strong> An opening that converted “cannot yet confirm” into “prohibited.”<br />\n<strong>What must travel with the prompt:</strong> The accurate rule, facts, intended audience, and material qualifications.<br />\n<strong>Limit:</strong> This improves the explanation; it does not establish that the underlying advice is correct.</p>\n</blockquote>\n<p>Someone reading that entry can understand why the method helped and where the lawyer still had to make a decision. Saving only the successful-looking paragraph would lose that lesson. The optional playbook form provides a place to record entries of your own.</p>\n"
      },
      {
        "h": "Keep rejected suggestions when they teach you something.",
        "html": "<p>Suppose a rewrite makes a recommendation easier to find but removes a condition that matters. Record both changes. The next prompt might ask for the clearer opening while expressly preserving the condition, followed by a comparison with the source.</p>\n<p>Be specific about the failure. “The answer was bad” will be difficult to use later. “The summary treated a witness's allegation as an established fact and gave no record location” identifies a problem you can look for again. It may also suggest a useful test for a recurring workflow.</p>\n<p>Keep decisions to work without AI as well. A small task may be easier to complete than to explain and review. An unfamiliar issue may require more of your own reading before assistance becomes useful. Those are judgments about the work, and they belong in the record alongside successful uses.</p>\n"
      },
      {
        "h": "Know where your work is saved.",
        "html": "<p>This guide saves entries in the browser profile you are using. It does not create an account, send your responses to Write.law, or make them available to an instructor or employer. The notes are yours to keep or share through a separate process.</p>\n<p>Use <strong>My saved work</strong> to download readable notes or a restorable backup. The readable file lets you review and share what you wrote. The backup preserves the saved state so you can restore it in another browser or at another site address. Restoring a backup replaces the entries in the destination browser, so preserve its current work first when you need both.</p>\n<p>Do not use the guide as a client file. Browser storage is not an approved confidential workspace, and someone using the same browser profile may be able to see the entries. Clearing browser data can remove them. The <a href=\"#/help?topic=saving\">help page</a> explains saving, recovery limits, and how to move work between devices.</p>\n"
      },
      {
        "h": "Choose a skill you want to practice independently.",
        "html": "<p>An assisted result can tell you something about the method without establishing what you can do alone. Keep track of both. You may want to become better at synthesizing a rule, explaining a difficult qualification, or recognizing when an argument has skipped a necessary step.</p>\n<p>Choose a small practice task and attempt it without AI. Then seek permitted feedback that helps you examine the attempt. Record what you could do independently and what the response helped you notice. A student can use this alongside course work; an experienced lawyer can use it to develop a skill in a new practice area or document type.</p>\n<p>Revisit the plan as your responsibilities change. The useful question is whether you are becoming better at the legal work and at directing assistance with it. Your playbook should make that progress easier to see.</p>\n"
      }
    ],
    "quiz": {
      "q": "You want another lawyer to reuse a successful prompt. What should accompany it?",
      "a": [
        "A description of how polished the first answer looked.",
        "An explanation of the task and sources, what you checked, and the limits you found when using it.",
        "The product name and a recommendation to use the same settings."
      ],
      "correct": 1,
      "why": "The prompt alone does not show why it worked or when it would be unsuitable. Preserve enough of the experience for someone else to judge whether it fits a different assignment."
    },
    "references": []
  },
  {
    "id": "leadership",
    "part": 3,
    "title": "Decide how the technology should change your work.",
    "nav": "Lead the work",
    "desc": "Better tools give lawyers more choices about how to deliver a service. We still need to decide which changes help clients, how people will learn, and who is responsible when something goes wrong.",
    "sources": [
      [
        "fall",
        "pp. 1–3, 17–18"
      ],
      [
        "student",
        "pp. 13–19"
      ]
    ],
    "sections": [
      {
        "h": "Examine what an existing practice is doing for people.",
        "html": "<p>A familiar task may serve more than one purpose. A junior lawyer's research helps answer the client's question, but it also develops the lawyer's ability to evaluate authority. A proposed automation might shorten the research while reducing that opportunity to learn. A responsible redesign needs to account for both effects.</p>\n<p>The same question applies to client service. A quicker document may be useful, but a client facing a difficult decision may also need time to ask questions and discuss consequences. Measure the change against the service you want to provide, rather than assuming that less production time answers every question.</p>\n<p>We should be willing to reconsider inherited practices. Some protect values that matter; others may persist because no one has examined them closely. Find out what a step contributes before deciding whether to preserve, change, or remove it.</p>\n\n<p>We should also ask what previously uneconomic solution could now exist. That question directs attention beyond the matters already arriving at a firm's door. Preventive services, small claims, and problems facing underserved communities may call for a different delivery model rather than a cheaper version of the same document. The possibility needs testing, boundaries, and a human path where required, but it belongs beside the discussion of risk.</p>\n<p>The broader questions about AI as an audience should remain questions rather than a recipe for manipulating a system. Can the legal point survive a summary? Does the writing connect the source with the proposition clearly enough for a human reviewer to inspect? How do we preserve nuance and minority views when several people use similar tools? The source invites lawyers to examine that changing environment without flattening the argument or trying to game the reader.</p>\n"
      },
      {
        "h": "Keep the profession's unresolved questions in view.",
        "html": "<p>What should legal work look like when producing answers becomes easier? We do not have final answers. Keeping those questions visible is part of the guidance rather than an assessment to complete.</p>\n<p>Consider what deserves a law license and what has been reserved to lawyers mainly by tradition. Consider which tasks exist because information used to be scarce and which forms of judgment remain important even when information is abundant. Those questions affect the design of services, regulation, and the opportunities a lawyer should investigate.</p>\n<p>The client questions are equally important. What should remain human because it involves trust, empathy, legitimacy, or the meaning of a person's life? How should fees reflect judgment, risk, availability, and access when production time falls? Who should receive the gains in time or cost, and who bears an error produced across several people and systems?</p>\n<p>There are also questions about institutions. How does advocacy change when AI may summarize or mediate the work before a person reads it? How will novices develop expertise when traditional training tasks are automated? Can technology improve access without scaling poor advice? How should lawyers lead teams that include clients, staff, experts, agents, and platforms?</p>\n<p>The <a href=\"#/questions\">questions for the profession</a> collect the source guides' broader inquiry by subject, including clients, public access, legal institutions, and law's role in an AI society. They are readable without selecting a question or writing a response. The optional reflection worksheet is there for readers who want to record how experience changes their views.</p>\n"
      },
      {
        "h": "Make it possible to question impressive-looking work.",
        "html": "<p>Someone needs to be able to say that a source is missing, a conclusion is overstated, or a workflow is not ready. That becomes harder when a team treats speed or visible AI use as the main sign of success.</p>\n<p>When a colleague identifies a problem, investigate how it arose. Was the assignment unclear? Did the reviewer lack access to the relevant source? Did an early assumption become difficult to question after several later steps relied on it? Those questions help you improve the process instead of treating every failure as an isolated mistake.</p>\n<p>Give people a workable way to pause an assignment and obtain a decision. Responsibility without enough time, information, or authority to act on it is difficult to exercise. Leaders should make the review possible, not merely require someone to sign off at the end.</p>\n\n<p>A mixed team needs more than instructions for the model. Clarify who is responsible for each handoff, who may challenge a conclusion, and who has the authority and time to investigate. Protect the ability to disagree even when the proposed answer appears unanimous because several systems produced similar prose. Agreement among tools does not remove the need for sources or accountable judgment.</p>\n"
      },
      {
        "h": "Judge progress by capabilities you can demonstrate.",
        "html": "<p>We can judge our progress through eight capabilities. You can <strong>frame before prompting</strong>, forming an initial map or theory and using AI to widen it. You can <strong>classify risk</strong>, distinguishing harm to others from harm to your own reasoning and choosing controls for the actual problem. You can <strong>verify</strong>, connecting authority, facts, reasoning, client fit, and process compliance with appropriate evidence.</p>\n<p>You can <strong>manage agents</strong> by specifying the work, allocating authority, setting feedback points, testing behavior, and returning uncertainty to a person. You can <strong>improve a process</strong> by mapping the service, removing waste, assigning work well, measuring the result, and revising it. You can <strong>build and test</strong> by translating a legal problem into requirements, exploring a prototype, identifying its limits, and governing deployment.</p>\n<p>You can <strong>lead</strong> by protecting candor, accountability, client value, and the public interest while the work changes. And you can <strong>own the result</strong> by explaining what the technology did, what you did, what you rejected, and why the final judgment is yours.</p>\n<p>These capabilities connect the whole guide. Knowing a product's newest feature is not the same as demonstrating them. Nor does checking every exercise establish them. The evidence is in your ability to direct the work, explain its basis, and improve the service someone actually receives.</p>\n"
      },
      {
        "h": "Carry one useful change into the next assignment.",
        "html": "<p>Look back at an exercise or note that changed how you approached the work. Describe the change in a way a colleague could use. Include the circumstance in which it helped and a limitation that someone reusing it should understand.</p>\n<p>Then choose the next thing to investigate. You might need a more specific drafting instruction, a better check for a recurring task, or time with someone whose experience reveals a problem you have overlooked. Keep the proposed step small enough that you can try it and learn from the result.</p>\n<p>That is how this guide is intended to be used beyond a course or workshop. Return to the explanations when you need them, adapt the methods to work you understand, and keep examining whether the assistance is making the legal service better.</p>\n"
      }
    ],
    "quiz": {
      "q": "How should a team judge whether a new AI-assisted process is worth keeping?",
      "a": [
        "Compare how many pages it produces each week.",
        "Examine whether it improves the client’s result and whether the team can review the work responsibly while developing its lawyers.",
        "Measure the proportion of assignments in which AI was used."
      ],
      "correct": 1,
      "why": "Output volume and adoption rates may describe activity without showing improvement. The guide asks teams to consider the quality of the service and the people responsible for delivering it."
    },
    "references": []
  }
];
const READING_QUESTIONS = [
  [
    "The profession",
    "The AI-Enabled Lawyer, p. 17",
    [
      "What work deserves a law license?",
      "Which legal tasks exist because information used to be scarce?",
      "What should remain human?",
      "What should become a product or process?",
      "How does advocacy change when AI reads first?",
      "What should clients pay for?",
      "How will novices become experts?",
      "Who bears the error?",
      "Who receives the gain?",
      "Can technology close the justice gap without scaling bad advice?",
      "How should lawyers lead mixed teams?",
      "What previously uneconomic solution can now exist?"
    ]
  ],
  [
    "AI and legal work",
    "AI for Law Students, pp. 13–14",
    [
      "Which parts of legal work are valuable because they produce an answer—and which are valuable because they force the lawyer to think?",
      "What happens when powerful, accurate legal analysis becomes abundant?",
      "Which tasks can be delegated to AI, and which decisions must remain attributable to a person? Where should we all agree that humans do the work?",
      "Will we change how we write, as humans, so that the AI tools reading our work handle it better?",
      "Will we change how we write to avoid “sounding like an AI”? Will we start writing more like AI because we read so much of it now?",
      "How much can a lawyer rely on an AI system without understanding how it reached its answer, particularly when tools do not show the steps?",
      "What does meaningful supervision look like when an agent performs hundreds of actions in minutes?",
      "When does using AI become part of competent representation so that not using it is an ethical violation?",
      "How should firms preserve institutional knowledge when much of the work occurs inside private AI conversations?",
      "Will AI reduce drudgery or merely increase expected output? Will it increase the data and paper we need to deal with?",
      "How do we preserve dissent when AI presents one polished recommendation as the natural answer? What happens if judges, lawyers, and clients use the same flawed tools?",
      "Will lawyers investigate less because AI can construct a plausible story from incomplete facts?",
      "What new kinds of legal work will AI create?"
    ]
  ],
  [
    "AI and clients",
    "AI for Law Students, pp. 14–15",
    [
      "Should clients decide whether AI is used in their matters?",
      "What must lawyers disclose about that use?",
      "Should clients receive the savings created by AI?",
      "Can clients understand enough about AI to consent meaningfully?",
      "Does a client have a right to speak with a human lawyer?",
      "Can a lawyer delegate emotionally or morally significant conversations to AI?",
      "What happens when an AI system knows more about the client than the lawyer does?",
      "Should AI infer goals the client has not expressed?",
      "Whose interests does the system serve when the client, lawyer, firm, insurer, and vendor want different things?",
      "Can an AI-generated recommendation subtly steer a client toward the outcome preferred by the lawyer or institution?",
      "How should lawyers protect clients whose vulnerabilities make them unusually susceptible to machine persuasion?",
      "What happens when a client relies on an AI summary instead of the lawyer’s actual advice?",
      "Who owns the client’s prompts, facts, strategy, and resulting work product?",
      "Can information shared with an AI remain confidential, privileged, and genuinely erasable?",
      "Should clients be able to inspect how AI influenced important advice or decisions?"
    ]
  ],
  [
    "AI and the public’s experience of law",
    "AI for Law Students, pp. 15–16",
    [
      "Does the public have a right to know when AI has shaped a government decision?",
      "Does a person have a right to a human hearing?",
      "How can someone challenge a decision when no person can explain how it was reached?",
      "Who helps people determine whether AI-generated legal advice is accurate?",
      "Should public-facing legal AI be regulated as information, software, or professional service?",
      "What remedies should exist when free or inexpensive legal AI causes harm?",
      "Can legal information be personalized without quietly becoming legal advice?",
      "Will AI make law understandable—or give people false confidence that they understand it?",
      "Can access to a chatbot substitute for access to representation?",
      "What happens when people can generate claims but cannot investigate, litigate, or enforce them?",
      "Will courts become less accessible if they assume everyone has AI assistance?",
      "Should public institutions provide an official legal AI rather than leaving access to private vendors?",
      "Must government systems support different languages, disabilities, literacy levels, and cultural contexts?",
      "Can AI help people comply with law before disputes arise?",
      "Could AI make rights practically usable rather than merely available on paper?",
      "How do we prevent landlords, employers, creditors, insurers, and governments from using AI to scale pressure faster than individuals can scale resistance?"
    ]
  ],
  [
    "AI and legal institutions",
    "AI for Law Students, pp. 16–17",
    [
      "Which exercises of state or government power may never be automated?",
      "Can the government rely on a proprietary system that the public cannot inspect?",
      "What process is due when an AI system affects liberty, benefits, employment, immigration status, or family integrity?",
      "Should judges disclose when AI helped analyze a case or draft an opinion?",
      "May judges use AI trained on material the parties never had an opportunity to address?",
      "What happens when different judges use different models to interpret the same law?",
      "Can AI-generated judicial reasoning create legitimate precedent?",
      "Will AI encourage courts to produce more decisions but devote less thought to each one?",
      "How should courts handle an explosion of inexpensive filings, discovery, and appeals?",
      "Can public defenders compete if prosecutors possess better models, data, and infrastructure?",
      "Should litigants have access to the tools used to investigate, score, prosecute, sentence, or supervise them?",
      "Can a government satisfy its duty to give reasons by offering an AI-generated explanation after the decision?",
      "Should legislatures use AI to model how proposed laws will affect different communities?",
      "Who is accountable when lawmakers adopt machine-generated language they do not fully understand?",
      "Can regulation remain democratic when technical complexity gives vendors more influence? How should lawyers consider vendors’ influence on the legal system?"
    ]
  ],
  [
    "Law’s role in an AI society",
    "AI for Law Students, pp. 17–19",
    [
      "Do people need a right to know when they are interacting with AI?",
      "Do people need a right to human review?",
      "Should people be able to refuse consequential AI decisions?",
      "Who owns a person’s voice, likeness, style, behavior, and inferred identity?",
      "Can privacy law protect people when AI can infer sensitive facts that were never collected?",
      "Should individuals be able to see, correct, or delete the profiles AI systems construct about them?",
      "May institutions treat people differently based on conduct an AI predicts but that has never occurred?",
      "How should discrimination law address harms produced by correlations rather than explicit classifications?",
      "When must a person be judged as an individual rather than as a member of a predicted group?",
      "Who owns the knowledge created from society’s collective writing, art, behavior, and experience?",
      "Should private companies control the infrastructure through which people learn, communicate, work, and obtain legal help?",
      "How much concentration of AI power is compatible with democracy?",
      "Should advanced AI be treated as a public utility, licensed profession, regulated product, or something new?",
      "Who may deploy systems capable of surveillance, persuasion, impersonation, or autonomous action?",
      "What duties should developers owe people who never agreed to use their systems?",
      "Should AI companies bear responsibility for foreseeable downstream uses of their products?",
      "How should liability work when harm emerges from interactions among developers, deployers, users, data, and autonomous agents?",
      "What evidence should a company need before releasing a system into high-stakes settings?",
      "How should law protect children growing up with AI tutors, companions, evaluators, and persuaders?",
      "What happens to freedom of thought when systems can predict which argument will influence each person?",
      "How should law respond when AI blurs the lines around what is verifiable evidence?",
      "Who should receive the wealth produced when AI draws upon generations of publicly created knowledge?",
      "What obligations do governments or others owe people and communities displaced by AI?",
      "Should efficiency gains produce shorter working lives, greater public wealth, or larger private returns?",
      "How do we preserve room for unusual, minority, and genuinely new ideas when AI favors statistically likely answers?",
      "What human capacities should society deliberately preserve even if machines can outperform us?",
      "How much environmental cost should society accept for AI systems?",
      "Can national law govern systems that operate globally?",
      "What happens when countries adopt radically different rules about autonomy, privacy, speech, and surveillance?",
      "Should future generations have representation in decisions about transformative AI?",
      "What rights might people need that existing constitutions never contemplated in an age of AI?",
      "Are we using AI to improve the legal and social order we want, or allowing available technology to choose that order for us?"
    ]
  ]
];
const SOURCE_COVERAGE = [
  [
    "The AI-Enabled Lawyer",
    "1–3",
    "Professional identity; frame, judge, design, counsel, challenge, own; expanded roles; systems fluency",
    "lawyer",
    "0–4",
    "Expanded reading"
  ],
  [
    "The AI-Enabled Lawyer",
    "4",
    "Human-first frame; AI-assisted expansion; lawyer-grade audit; human revision and judgment; document and improve",
    "method",
    "4",
    "Full five-stage explanation"
  ],
  [
    "The AI-Enabled Lawyer",
    "5",
    "Five questions before prompting; green/yellow/red levels of control",
    "permission",
    "0–1",
    "All questions and categories in the reading"
  ],
  [
    "The AI-Enabled Lawyer",
    "6",
    "External and internal risk; four combinations and matching controls",
    "permission",
    "2",
    "All four situations explained"
  ],
  [
    "The AI-Enabled Lawyer",
    "7",
    "Six forms of purposeful friction, including divergence, adversarial prompting, reviewed sources, distance, and annotated reliance",
    "think",
    "1–4",
    "Expanded reading"
  ],
  [
    "The AI-Enabled Lawyer",
    "8",
    "Seven professional duties and subordinate-lawyer responsibility",
    "ethics",
    "0–4",
    "Reading plus linked primary authority"
  ],
  [
    "The AI-Enabled Lawyer",
    "9",
    "Learning through human-first work and questions before replacement prose",
    "think",
    "0–4",
    "Reading and visible tutor example"
  ],
  [
    "The AI-Enabled Lawyer",
    "10",
    "Eight management functions and six management failures",
    "agents",
    "0–4",
    "Full reading; failures named and explained"
  ],
  [
    "The AI-Enabled Lawyer",
    "11",
    "The twelve-part agent work order",
    "agents",
    "1",
    "Complete readable reference and worked assignment"
  ],
  [
    "The AI-Enabled Lawyer",
    "12–13",
    "Nine process stages; user, outcome, sequence, judgment, control, learning; NIST perspective",
    "process",
    "0–4",
    "Full reading"
  ],
  [
    "The AI-Enabled Lawyer",
    "14",
    "Ten harness elements; staged sequence; limits of cross-model critique",
    "harness",
    "0–4",
    "Full reading"
  ],
  [
    "The AI-Enabled Lawyer",
    "15",
    "Six lawyer contributions to building and six prototype-to-pilot standards",
    "building",
    "0–4",
    "Full reading, no checklist required"
  ],
  [
    "The AI-Enabled Lawyer",
    "16",
    "Six parts of a lawyering playbook",
    "playbook",
    "0–4",
    "Full reading and prepared entry"
  ],
  [
    "The AI-Enabled Lawyer",
    "17",
    "Twelve open professional questions",
    "leadership",
    "0–2",
    "Reading and complete question reference"
  ],
  [
    "The AI-Enabled Lawyer",
    "18",
    "Eight closing capabilities and the profession’s wider imagination and reach",
    "leadership",
    "3–4",
    "Full reading"
  ],
  [
    "Using AI This Semester",
    "1",
    "Twelve before/during/after practices",
    "permission; method; ethics; think",
    "multiple",
    "Distributed across relevant chapters; source checklist retained"
  ],
  [
    "Using AI This Semester",
    "2",
    "Five self-assessment questions; accept/modify/reject; limits of research claim",
    "think",
    "1",
    "All questions and method visible"
  ],
  [
    "Using AI This Semester",
    "2",
    "Seven stopping circumstances",
    "permission",
    "3",
    "All circumstances visible"
  ],
  [
    "Using AI This Semester",
    "2",
    "Use note and limits of disclosure as a substitute for review",
    "ethics",
    "3–4",
    "Visible example"
  ],
  [
    "AI for Law Students",
    "1–2",
    "Language and lawyer value; opportunity beyond efficiency; independence; shaping norms",
    "lawyer; leadership",
    "multiple",
    "Expanded reading, mixed-audience framing"
  ],
  [
    "AI for Law Students",
    "2–4",
    "Training, tokens, parameters, post-training, tools, generation, variation, uneven capability",
    "basics",
    "0–4",
    "Full conceptual explanation"
  ],
  [
    "AI for Law Students",
    "4–6",
    "Models versus applications; context, saved references, prompting as assignment; memory",
    "basics; harness; prompting",
    "multiple",
    "Full reading, product limits distinguished"
  ],
  [
    "AI for Law Students",
    "6–8",
    "Hallucination, source verification, retrieval, reasoning models, agents, harnesses",
    "basics; agents; harness",
    "multiple",
    "Full concepts; historical case counts not recast as current data"
  ],
  [
    "AI for Law Students",
    "9–10",
    "Practice uses and product categories",
    "basics; writing",
    "multiple",
    "Categories and uses explained; historical vendors not a buying guide"
  ],
  [
    "AI for Law Students",
    "10–11",
    "Professional duties, court requirements, confidential information",
    "ethics; permission",
    "multiple",
    "Reading and linked primary references"
  ],
  [
    "AI for Law Students",
    "11–12",
    "Learning rather than outsourcing; tutoring, role-play, challenge, feedback",
    "think; method",
    "multiple",
    "Reading; optional activities remain supplementary"
  ],
  [
    "AI for Law Students",
    "12–13",
    "Exploration suggestions and further-reading resources",
    "sources; think; method",
    "multiple",
    "Concepts in reading; bibliographic leads retained in source notes"
  ],
  [
    "AI for Law Students",
    "13–19",
    "All five groups of open questions",
    "questions",
    "all",
    "Complete readable collection with minor copyediting"
  ],
  [
    "AI for Law Students",
    "19–22",
    "Glossary",
    "glossary",
    "all",
    "Missing vocabulary restored; current-status claims not repeated as current fact"
  ],
  [
    "Leveling Up Your AI Prompting",
    "2–3",
    "Iterative engagement; process; when, how, and improvement over time",
    "method; playbook",
    "multiple",
    "Full reading"
  ],
  [
    "Leveling Up Your AI Prompting",
    "4–7",
    "Three opportunities; first work; limits on uses you cannot judge; guidance",
    "lawyer; permission; prompting",
    "multiple",
    "All opportunities and decision limits explained"
  ],
  [
    "Leveling Up Your AI Prompting",
    "8–10",
    "Six collaboration practices; variable amount of human-first work",
    "method; think",
    "multiple",
    "All six practices in plain reading"
  ],
  [
    "Leveling Up Your AI Prompting",
    "11–13",
    "Employee-departure facts and AI prioritization comparison",
    "think",
    "2",
    "Complete fact passage and visible comparison; no exercise required"
  ],
  [
    "Leveling Up Your AI Prompting",
    "14–19",
    "Direct/context/show; expand/pressure-test/identify; options and follow-up",
    "method; prompting",
    "multiple",
    "Full reading"
  ],
  [
    "Leveling Up Your AI Prompting",
    "20–24",
    "Fee-table original and different prompt results",
    "writing",
    "1",
    "Original and all three principal comparisons visible"
  ],
  [
    "Leveling Up Your AI Prompting",
    "25–31",
    "Scale for model and reviewer; isolate headings or subject line",
    "method",
    "3",
    "Reading and concrete examples"
  ],
  [
    "Leveling Up Your AI Prompting",
    "32–39",
    "Ten principles; variables; priority; quoted material; self-checking; reuse; style specification",
    "prompting; aiisms",
    "multiple",
    "Full reading with qualifications recorded"
  ],
  [
    "Leveling Up Your AI Prompting",
    "40–53",
    "Dog-toy introduction, concrete narration, annotated exemplars, diagnosis/candidates/evaluation/explanation/choice",
    "writing",
    "2",
    "Visible before/opinion excerpt and process explanation"
  ],
  [
    "Leveling Up Your AI Prompting",
    "54",
    "AI assistance at multiple points inside research and analysis",
    "method",
    "1–2",
    "Reading"
  ],
  [
    "Leveling Up Your AI Prompting",
    "55–57",
    "Stonebridge and Falcon material facts and conditions",
    "writing",
    "3–4",
    "Complete originals and clearly identified prepared revisions"
  ],
  [
    "Leveling Up Your AI Prompting",
    "58–65",
    "Two ways to address AI-isms; words, sentences, formatting, substance",
    "aiisms",
    "0–4",
    "Full reading"
  ],
  [
    "Leveling Up Your AI Prompting",
    "66",
    "Data-retention before/after illustration",
    "aiisms; sources",
    "3",
    "Unsupported legal ceiling and enforcement details not adopted; limitation explicit"
  ],
  [
    "Leveling Up Your AI Prompting",
    "67–72",
    "Weak employment paragraph and authorship-contrast exercises",
    "aiisms",
    "2",
    "Weak paragraph and diagnosis visible; no authorship detector implied"
  ],
  [
    "Leveling Up Your AI Prompting",
    "73–77",
    "Own style, house style, challenge the description, save style block",
    "aiisms",
    "4",
    "Full reading"
  ],
  [
    "Leveling Up Your AI Prompting",
    "78–87",
    "Rewriting, editing, drafting, summarizing, organizing, analysis, learning, playbooks, checklists",
    "writing; method; playbook",
    "multiple",
    "Uses integrated in reading; heading-only example slides do not supply missing examples"
  ],
  [
    "Original graphing discussion",
    "whole guide",
    "Dependencies, parallel work, source-linked handoffs, stop/return paths, human decisions, manual operation, tests, automation",
    "graphing",
    "0–8",
    "Complete worked sequence available without running the simulation"
  ]
];
const EDITORIAL_DECISIONS = [
  "The four subject areas and each numbered framework retain separate functions. A workflow map, a knowledge graph, the five-stage responsible-use process, six collaboration practices, ten prompting principles, and twelve-part work order are not merged.",
  "Chapter and section addresses, activity IDs, the local-storage key, and the backup identifier are preserved. Optional companion forms retain existing saved field keys.",
  "Prepared advice revisions and added workflow examples are identified as guide additions. Original Stonebridge, Falcon, fee-table, employee-departure, and deliberately weak AI-isms passages retain their supplied meaning and qualifications.",
  "The original slide on a supposed three-year GDPR ceiling and a specific enforcement penalty supplies no supporting authority. Those legal assertions are not adopted as law. The guide explicitly explains that limitation rather than replacing them with invented support.",
  "The employment “What we found” slide refers to a Vance passage and a word count that do not match the immediately preceding Ms. Chen paragraph. Its diagnosis is not presented as a verbatim answer key to that paragraph; the guide identifies its own explanation as prepared commentary.",
  "Some slides supply only an “Example” heading. The guide does not pretend that those slides contain a worked example. The developed examples in the reading are identified by source or as guide additions.",
  "The introductory PDF’s historical model names, adoption figures, sanctions totals, product guarantees, and legal-tool benchmark rates have not been freshly verified. They are not presented as current statistics or product recommendations. Core distinctions and the category map remain in the reading.",
  "The source’s strong prohibitions on unreviewable work and its red/yellow/green framing remain substantive guidance. A color or completed form is not treated as permission, and jurisdiction-specific professional duties require the actual authority.",
  "The source’s short-term-memory and system-prompt explanations describe different products at a high level. The guide distinguishes a saved reference arrangement from software-enforced controls and does not promise that a folder enforces permissions.",
  "The fixed rhythm and numerical voice-vector examples are identified as illustrative variables, not mandatory style rules. The user’s express request for full sentences and natural, non-formulaic prose governs this edition.",
  "The four-minute pause remains a suggested teaching practice. The source itself limits the inference from research with science students; the guide retains that qualification.",
  "The source’s questions are open inquiries, not established legal conclusions or a grading rubric. The full readable reference restores questions previously available only as selected reflection prompts. Minor punctuation and obvious typographical errors are edited without supplying answers.",
  "The source glossary is expanded for readable use. Historical claims about what has or has not been achieved are not converted into current assertions. The technical vocabulary is explanatory, not an endorsement of any product.",
  "The legal note about the full text of Model Rule 5.2 is a separately sourced clarification, not language attributed to the teaching slides. Primary references remain distinguishable from the author’s teaching material."
];
