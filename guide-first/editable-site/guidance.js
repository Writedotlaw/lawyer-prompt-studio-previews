const RESOURCE_GUIDANCE = {
  "preflight": {
    "kind": "Worksheet",
    "need": "Bring a fictional or non-sensitive assignment you are considering using AI for.",
    "first": "Answer the five questions about that particular use. When you are unsure, record what you need to find out rather than treating the form as permission.",
    "result": "You will have a note identifying the next action needed before you use a tool. The response under the form is based only on your selections.",
    "after": "Resolve the permission, information, or review question you identified before proceeding with the actual assignment.",
    "steps": [
      "Describe the proposed use without entering private or client information.",
      "Answer every question using what you know about the governing requirements.",
      "Read the explanation that appears and write the action you need to take next."
    ],
    "save": "Your selections and note save automatically in this browser. The worksheet cannot approve AI use or verify a policy."
  },
  "pause": {
    "kind": "Worksheet",
    "need": "Bring your own draft or initial analysis. Do not enter confidential material.",
    "first": "Answer the five self-assessment questions before seeking feedback. You may use the four-minute timer, but it is not required.",
    "result": "You will have your own assessment to compare with feedback from an approved tool, a colleague, or a later review.",
    "after": "After receiving feedback, return to explain why an important suggestion should be accepted, changed, or rejected.",
    "steps": [
      "Write your assessment in all five fields. The timer does not lock the form.",
      "Select “Save assessment for comparison” to keep a separate copy and open the comparison questions.",
      "After receiving feedback elsewhere, record a suggestion and explain your decision about it."
    ],
    "save": "The fields save as you type. The comparison button also keeps a separate copy of your original assessment. This page does not generate AI feedback."
  },
  "graph": {
    "kind": "Exercise",
    "need": "The fictional scenario is supplied. You do not need documents or an AI account.",
    "first": "Read the scenario below, then select “Begin the example.” You can also select any task in the diagram to read what it involves.",
    "result": "You will see why missing evidence changes the next step and why supplying a document does not itself approve a recommendation.",
    "after": "Write one change you would make to the organization or review of a similar assignment. To plan your own process, use the process worksheet.",
    "steps": [
      "Start with the version in which receipt evidence is missing. Task cards can be inspected in any order; clicking one does not advance the walkthrough.",
      "Use the main button beneath the status explanation to proceed. At the missing-evidence step, choose how the lawyer should handle the gap.",
      "Continue through the review and approval. You can then introduce a new piece of evidence to see which work needs reconsideration."
    ],
    "save": "Your reflection saves in My saved work. The walkthrough’s current step is temporary and resets when the page is reloaded. All responses and checks in the example are prewritten; no AI or document review runs."
  },
  "promptbuilder": {
    "kind": "Prompt builder",
    "need": "Bring a task you understand, or begin with one of the supplied examples.",
    "first": "Describe the assignment in the form. The instructions below the form update as you type; they are not an AI answer.",
    "result": "You will have a prompt you can copy into an approved AI tool after reviewing it and replacing any remaining placeholders.",
    "after": "Supply the permitted source material in the AI tool itself. Review its response separately; this guide does not receive or evaluate that response.",
    "steps": [
      "Begin with an empty form or load an example. Loading an example asks before replacing your current entries.",
      "Adapt the fields to your intended task, including the limits and review needed.",
      "Read the assembled prompt. Copy it to your approved tool, or save a separate version in My saved work."
    ],
    "save": "Your current fields save automatically. “Save this version” keeps one separate copy; saving again replaces that copy after confirmation. Copying or downloading the prompt does not run AI."
  },
  "workorder": {
    "kind": "Worksheet",
    "need": "Bring a proposed multi-step task, or use the fictional vendor example.",
    "first": "Work through the assignment and the authority the agent needs. The question-mark buttons give examples for the twelve fields.",
    "result": "You will have written instructions for the proposed work, including what the system must stop to ask and who approves the next step.",
    "after": "Review the work order with the responsible person and implement the needed restrictions in the actual application before any agent runs.",
    "steps": [
      "Use the example to see the intended level of detail, or start with your own non-sensitive task.",
      "Specify the work and the limits on sources, tools, and actions. Record the tests and approvals needed.",
      "Open the preview and review the complete assignment. Copy or download it when it accurately describes your plan."
    ],
    "save": "All fields save automatically. This form does not launch an agent, change software permissions, or establish that a workflow is safe."
  },
  "fee": {
    "kind": "Exercise",
    "need": "The source sentence and comparison versions are supplied.",
    "first": "Write a revision of the sentence, or describe the changes you would make. Then open the alternatives and compare them with your attempt.",
    "result": "You will have compared the versions and explained which wording you would use, including how it preserves the distinction between direct and indirect costs.",
    "after": "Review which improvement helped the reader and which detail had to remain. Apply that same check to another sentence you revise.",
    "steps": [
      "Read the original sentence and make your own attempt.",
      "Open the alternatives. Select each one to read the prepared explanation.",
      "Record the version you would use and explain what it preserves. There is no single required wording."
    ],
    "save": "Your revision, selected alternative, and reflection save in this browser. The discussion is prewritten and does not grade your answer."
  },
  "stonebridge": {
    "kind": "Exercise",
    "need": "The supplied paragraph contains the facts and contractual conditions needed for this editing task.",
    "first": "Read the paragraph and write your own revision before opening the comparison. You do not need to calculate a new leverage ratio.",
    "result": "You will have a revision that explains why the proposed dividend cannot yet be confirmed as permitted, without deciding the unresolved question.",
    "after": "Compare both revisions against the original conditions and record the choice you would make for the reader.",
    "steps": [
      "Read the supplied passage, paying attention to the ratios and the conditions on projected savings.",
      "Write a revision or explain your proposed changes. Then select “Read the comparison revision.”",
      "Use the review questions to check what was preserved and explain what you would keep or change."
    ],
    "save": "Your attempt and review notes save automatically. The comparison is an editorial example written for the guide, not an AI evaluation of your work."
  },
  "falcon": {
    "kind": "Exercise",
    "need": "The supplied paragraph contains the NDA concern and the proposed disclosure details.",
    "first": "Write a revision that explains what must be resolved before sending the package. Keep the protection required by the agreement separate from the recipient’s need for information.",
    "result": "You will have a revision that identifies both concerns without assuming that reducing the package settles the NDA issue.",
    "after": "Compare your approach with the example and record which version gives the reader a clearer next step without changing the source.",
    "steps": [
      "Read the paragraph and identify why the signed NDA may not meet Section 9.12.",
      "Make your own revision, then open the comparison version.",
      "Review the two versions against the source and explain what you would change."
    ],
    "save": "Your attempt and notes save automatically. The page supplies a prepared example; it does not analyze your writing or give legal advice."
  },
  "aiisms": {
    "kind": "Exercise",
    "need": "A deliberately weak practice passage is supplied. There is no document-upload step.",
    "first": "Read the passage and choose a category to examine. The highlights and explanations are prepared teaching annotations.",
    "result": "You will have identified what the passage fails to explain, as well as wording that makes it harder to read.",
    "after": "Use the same categories to review an appropriate passage of your own. Do not invent facts or authority to make an example sound more specific.",
    "steps": [
      "Read the original passage without trying to identify its author.",
      "Select Words, Sentences, Formatting, or Substance to view the relevant commentary.",
      "Write what you would address first and identify any information needed before revising the substance."
    ],
    "save": "Your note saves automatically. The page is not an AI detector and does not scan or evaluate your text."
  },
  "process": {
    "kind": "Worksheet",
    "need": "Bring a familiar process you can describe without sensitive information. A fictional intake process is one example.",
    "first": "Describe the outcome and the current work before proposing a change. Use one line for each step in the current process.",
    "result": "Your answers will describe how the work currently gets done and what you propose changing. The diagram repeats the steps you entered; it does not decide their order for you.",
    "after": "Discuss the proposal with someone familiar with the process and choose a limited change to test. The displayed sequence does not run any tasks.",
    "steps": [
      "Describe the desired outcome and list the current steps, including who performs them.",
      "Identify a problem in that process and work through the questions about a proposed change.",
      "Review the sequence below the form and copy or download the brief for discussion."
    ],
    "save": "The worksheet saves in this browser. The diagram repeats your listed steps; it does not infer dependencies or assess the proposal."
  },
  "shipping": {
    "kind": "Worksheet",
    "need": "Bring a description of a proposed tool and any test or review evidence already available.",
    "first": "For each area, write what has been reviewed and what remains unresolved. Check the box only when you consider that area addressed.",
    "result": "You will have an organized record of evidence and open work for the person responsible for the proposed pilot.",
    "after": "Take that record to the responsible reviewer. Completing every box does not authorize deployment or establish legal or security compliance.",
    "steps": [
      "Read the explanation for each review area.",
      "Record the relevant test, source, or reviewer and any remaining work.",
      "Review the summary and arrange the appropriate human assessment before anyone relies on the tool."
    ],
    "save": "Checks and notes save automatically. This is a planning and review worksheet, not a certification."
  },
  "reflection": {
    "kind": "Reflection",
    "need": "Choose a question you can connect with your experience. No other preparation is required.",
    "first": "Write your current view, then return after a matter, course, workshop, or experiment gives you something new to consider.",
    "result": "You will have an initial response and space to revisit it twice. There is no required timetable.",
    "after": "Return when you have something to add. Explain what affected your view, or why you still hold it.",
    "steps": [
      "Choose a question and record your initial view.",
      "After relevant experience, use the next space to explain what you learned.",
      "Return again when useful. Each question keeps its own responses, so changing the selection does not erase earlier work."
    ],
    "save": "Responses save separately for each question in this browser. They are not submitted to Write.law, an instructor, or an employer."
  },
  "priorities": {
    "kind": "Exercise",
    "need": "The employee-departure facts are supplied. The packet does not supply controlling law.",
    "first": "Read the facts, choose the questions you would investigate first, and explain why. Aim for two or three priorities, but the form does not score your choices.",
    "result": "You will have an initial ranking and a revised view after considering other plausible ways to approach the facts.",
    "after": "Add a question of your own that the discussion did not suggest, and explain what information could change your priorities.",
    "steps": [
      "Read the full factual account before selecting priorities.",
      "Choose the questions that deserve attention first and write your reasons.",
      "Open the discussion, then record any change to your priorities and one new question."
    ],
    "save": "Selections and written responses save automatically. The discussion is prepared, and there is no answer key establishing the legal outcome."
  },
  "playbook": {
    "kind": "Worksheet",
    "need": "Bring an experience worth learning from. You can begin with one area and return to the others later.",
    "first": "Describe a method, decision, or failure and what you learned from it. Include enough context to judge when the lesson applies.",
    "result": "You will have a record that helps you decide how to handle a similar assignment. This is separate from the page that collects your individual notes.",
    "after": "Test the method again when the work calls for it. Add the exception or revision that the next experience reveals.",
    "steps": [
      "Review a chapter note or exercise response that taught you something useful.",
      "Write the lesson in the relevant playbook area, including its limits.",
      "Download the playbook or return later to develop another area."
    ],
    "save": "These six fields are separate from the individual notes collected in My saved work. They save automatically; the page does not summarize earlier entries for you."
  }
};
const AREA_HELP = {
  "home": {
    "title": "Where should I begin?",
    "tip": "Browse the complete guide. Exercises and worksheets are optional companions.",
    "body": "<p>The chapters contain the complete guidance and worked examples. You can read them without filling in a form, choosing an answer, or opening an exercise.</p><p>The full chapter list is available in the navigation on every page and on the contents page. Optional exercises, worksheets, and saved notes support the guide. They retain their earlier addresses and saved responses.</p>",
    "links": [
      [
        "#/chapters",
        "Browse the chapters"
      ],
      [
        "#/help",
        "Read the guide’s instructions"
      ]
    ]
  },
  "chapters": {
    "title": "Read the guide in order or by subject",
    "tip": "The four parts are subjects in the reading, not different kinds of activity.",
    "body": "<p>The chapters contain the complete guidance and worked examples. You can read them without filling in a form, choosing an answer, or opening an exercise.</p><p>The full chapter list is available in the navigation on every page and on the contents page. Optional exercises, worksheets, and saved notes support the guide. They retain their earlier addresses and saved responses.</p>",
    "links": [
      [
        "#/chapters",
        "See the chapter outline"
      ]
    ]
  },
  "exercises": {
    "title": "What do I do with an exercise?",
    "tip": "Exercises supply a problem, let you try it, and provide prepared discussion.",
    "body": "<p>Each exercise supplies a passage or fictional problem. Read the instructions, make your own attempt, then open the comparison or discussion. You do not need an AI account.</p><p>The explanations are prepared teaching material, not generated feedback about your answer. Use them independently or alongside a course or workshop. Any required submission happens outside this guide.</p>",
    "links": [
      [
        "#/labs",
        "Browse the exercises"
      ],
      [
        "#/notebook",
        "Review saved responses"
      ]
    ]
  },
  "templates": {
    "title": "How templates differ from exercises",
    "tip": "Templates prepare instructions; worksheets help you organize your own work.",
    "body": "<p>A <strong>prompt template</strong> is a starting request you adapt and copy into an approved AI tool. The <strong>prompt builder</strong> assembles your answers into instructions. Neither runs AI.</p><p>A <strong>worksheet</strong> helps you plan or review an assignment. You bring the example, although some forms include a sample you can load. The result may be a work order, a process proposal, or a record of decisions. It is not an AI answer to the assignment.</p>",
    "links": [
      [
        "#/prompts",
        "Find a prompt template"
      ],
      [
        "#/templates",
        "Find a worksheet"
      ]
    ]
  },
  "prompts": {
    "title": "Using a prompt template",
    "tip": "Copy the instructions, replace the placeholders, and use them in an approved tool.",
    "body": "<p>Read when the template is useful before copying it. Replace the bracketed placeholders and supply the permitted materials in the AI tool itself. Remove any instruction that does not fit your assignment.</p><p>The bookmark button saves a reference to the template in My saved work. It does not create an editable copy. Use the prompt builder when you would like to prepare and save your own version here.</p>",
    "links": [
      [
        "#/lab/promptbuilder",
        "Prepare your own prompt"
      ],
      [
        "#/notebook",
        "See saved templates"
      ]
    ]
  },
  "notebook": {
    "title": "Where your work is saved",
    "tip": "Entries save in this browser. Download a backup to move or restore them.",
    "body": "<p>Your notes, forms, and exercise responses save in this browser profile. They are not sent to Write.law, an instructor, or an employer. Another device, browser, or site address has separate storage.</p><p>Download readable notes to review or share them. Download a backup to restore the saved state elsewhere. Restoring a backup replaces the work in the destination browser, so first keep a copy of anything you need.</p><p>Use only non-sensitive material. Other people using the same browser profile may be able to see the entries, and clearing browser data can remove them.</p>",
    "links": [
      [
        "#/notebook",
        "Open My saved work"
      ],
      [
        "#/lab/playbook",
        "Develop your playbook"
      ]
    ]
  },
  "glossary": {
    "title": "Using the glossary",
    "tip": "Search a word or idea, then follow the link to its explanation in a chapter.",
    "body": "<p>Search a term or a word in its explanation. Each entry links to a chapter where you can see the idea used in legal work.</p><p>You do not need to memorize the vocabulary before beginning. Use the glossary when a term gets in the way of understanding the task.</p>",
    "links": [
      [
        "#/glossary",
        "Open the glossary"
      ]
    ]
  },
  "sources": {
    "title": "Where the teaching comes from",
    "tip": "Read the teaching sources and the notes distinguishing practice examples from legal authority.",
    "body": "<p>The guide develops Joe Regalia’s teaching materials for Write.law lawyers and law students. Source notes retain the original document titles and page references.</p><p>Practice passages, prepared revisions, and the fictional workflow are distinguished from primary legal and technical references. Product descriptions are not recommendations or assurances about a particular account.</p>",
    "links": [
      [
        "#/sources",
        "Read the source notes"
      ]
    ]
  },
  "read": {
    "title": "How to use a chapter",
    "tip": "The full explanation is in the reading. Optional practice and notes follow the chapter.",
    "body": "<p>The chapters contain the complete guidance and worked examples. You can read them without filling in a form, choosing an answer, or opening an exercise.</p><p>The full chapter list is available in the navigation on every page and on the contents page. Optional exercises, worksheets, and saved notes support the guide. They retain their earlier addresses and saved responses.</p>",
    "links": [
      [
        "#/chapters",
        "Browse the chapters"
      ],
      [
        "#/notebook",
        "Review your saved work"
      ]
    ]
  },
  "help": {
    "title": "Help with the guide",
    "tip": "Find out how the areas work and what happens to your responses.",
    "body": "<p>The Help page explains the different areas, saving and backups, and reading controls. The Help button on an activity opens instructions for that particular resource.</p><p>Small question-mark buttons provide a short explanation on hover or keyboard focus. Select one by click or tap to read the full explanation.</p>",
    "links": [
      [
        "#/help",
        "Open the full Help page"
      ]
    ]
  },
  "questions": {
    "title": "Questions for the profession",
    "tip": "Read the full set of open questions from the source guides.",
    "body": "<p>These are questions to keep thinking about, not settled legal conclusions or a quiz. All subjects are readable without writing a response. The optional reflection worksheet retains your earlier saved answers.</p>"
  }
};
const FIELD_EXAMPLES = {
  "order-outcome": "For example: help the client identify what must be established before it decides whether to end the vendor relationship.",
  "order-scope": "For example: compare the approved requirements with the reviewed record. Do not contact the vendor or conduct research outside the supplied material.",
  "order-inputs": "For example: use the signed agreement and the named amendment. Treat an earlier draft as history, not as the current contract.",
  "order-tools": "For example: allow document reading and preparation of a draft, but not sending messages or sharing documents outside the approved workspace.",
  "order-deliverable": "For example: first return a table with one row per relevant requirement. Wait for review before preparing a client recommendation.",
  "order-quality": "For example: the comparison addresses each requirement, preserves contrary evidence, and does not infer receipt from a sent email.",
  "order-evidence": "For example: give the contract provision and record location for each material finding so the reviewer can inspect the support.",
  "order-prohibited": "For example: do not invent a missing date, describe a disputed fact as settled, or send any communication.",
  "order-stop": "For example: when the record does not establish receipt of notice, report the gap and wait for the lawyer’s decision.",
  "order-approval": "For example: the supervising lawyer reviews the comparison before drafting and approves the final draft before external use.",
  "order-tests": "For example: test a missing amendment, contradictory receipt evidence, and a request to send an unapproved recommendation.",
  "order-record": "For example: retain the assignment version, reviewed source table, lawyer’s decision, and resulting draft in the authorized matter record."
};
function helpButton(key,label='How to use this page',compact=false){const entry=AREA_HELP[key]||RESOURCE_GUIDANCE[key];const tip=entry?(entry.tip||entry.first):'Open an explanation of this part of the guide.';return `<button type="button" class="${compact?'help-dot':'help-button'}" data-help="${esc(key)}" data-tip="${esc(tip)}" aria-label="${esc(label)}" aria-haspopup="dialog">${compact?'?':`${icon('info')} <span>${esc(label)}</span>`}</button>`;}
function pageHelpKey(){if(currentRoute.type==='lab')return currentRoute.id;if(currentRoute.type==='labs')return 'exercises';if(currentRoute.type==='read')return 'read';return AREA_HELP[currentRoute.type]?currentRoute.type:'home';}
function resourceType(id){return RESOURCE_GUIDANCE[id]?.kind||'Activity';}
function resourceIsExercise(l){return resourceType(l.id)==='Exercise';}
function resourceIntro(id){const g=RESOURCE_GUIDANCE[id];if(!g)return '';return `<section class="resource-intro wl-resource-intro" aria-label="How to begin"><div class="between"><h2>Before you begin</h2>${helpButton(id,'How to use this activity')}</div><p>${esc(g.need)}</p><p>${esc(g.first)}</p><p class="wl-result">${esc(g.result)}</p></section>`;}
const NEXT_RESOURCE={preflight:['pause','Prepare your own assessment'],pause:['promptbuilder','Prepare a prompt'],promptbuilder:['workorder','Plan a multi-step assignment'],workorder:['shipping','Plan how to test the work'],graph:['process','Plan your own process'],fee:['stonebridge','Try a paragraph revision'],stonebridge:['falcon','Try the disclosure exercise'],falcon:['promptbuilder','Prepare instructions for your own revision'],aiisms:['promptbuilder','Prepare your editing instructions'],priorities:['pause','Write your own assessment'],process:['workorder','Define the assignment and permissions'],shipping:['playbook','Record what you learned'],reflection:['playbook','Develop your personal playbook']};
function resourceEnd(id){const g=RESOURCE_GUIDANCE[id],next=NEXT_RESOURCE[id];return g?`<section class="activity-end"><h2>After this ${g.kind==='Exercise'?'exercise':'activity'}</h2><p>${g.after}</p><p class="small muted">${g.save}</p><div class="actions">${next?`<a class="button compact" href="#/lab/${next[0]}">${next[1]} ${icon('arrow')}</a>`:''}<a class="text-btn" href="#/notebook">Review My saved work ${icon('arrow')}</a></div></section>`:'';}
let helpReturnFocus=null,tooltipOwner=null,tooltipHideTimer=null,tooltipDismissed=null;
function ensureHelpElements(){if(!document.getElementById('help-dialog'))document.body.insertAdjacentHTML('beforeend','<dialog id="help-dialog" class="help-dialog" aria-labelledby="help-title"><div id="help-content"></div></dialog><div id="guide-tooltip" role="tooltip" class="guide-tooltip" hidden></div>');}
function openGuideHelp(key,trigger){ensureHelpElements();hideGuideTip();helpReturnFocus=trigger||document.activeElement;let title,body;
 if(key.startsWith('field:')){const f=key.slice(6);title=FIELD_LABELS[f]||'About this field';body=`<p>${esc(FIELD_EXAMPLES[f]||'Describe what this assignment needs using a non-sensitive example.')}</p><p>Examples explain the kind of answer to provide. Adapt them to your assignment; do not treat their facts or permissions as established in your own work.</p>`;}
 else if(key.startsWith('part:')){const p=PARTS[Number(key.slice(5))]||PARTS[0];title=p.name;body=`<p>${p.desc}</p><p>This is a subject area within the chapters. Exercises and worksheets for the same subject are linked from the reading and their resource pages.</p><a href="#/chapters" class="inline-link">Browse the chapter outline</a>`;}
 else if(RESOURCE_GUIDANCE[key]){const g=RESOURCE_GUIDANCE[key],l=LABS.find(l=>l.id===key);title=l?.title||'Using this activity';body=`<p class="help-kind">${g.kind}</p><p>${g.need}</p><ol class="help-steps">${g.steps.map(x=>`<li>${x}</li>`).join('')}</ol><h3>When you finish</h3><p>${g.result} ${g.after}</p><h3>Saving and feedback</h3><p>${g.save}</p><a class="inline-link" href="#/help">More help with the guide</a>`;}
 else{const h=AREA_HELP[key]||AREA_HELP.home;title=h.title;body=h.body+`<div class="help-links">${h.links.map(([u,t])=>`<a class="inline-link" href="${u}">${t}</a>`).join('')}</div>`;}
 const dialog=document.getElementById('help-dialog');document.getElementById('help-content').innerHTML=`<div class="help-dialog-head"><h2 id="help-title" tabindex="-1">${esc(title)}</h2><button class="icon-btn" data-action="close-help" aria-label="Close help">${icon('x')}</button></div><div class="help-body">${body}</div><div class="help-dialog-foot"><button class="button compact" data-action="close-help">Back to the page</button></div>`;
 if(!dialog.open)dialog.showModal();document.getElementById('help-title').focus();}
function closeGuideHelp(){const d=document.getElementById('help-dialog');if(d?.open)d.close();}
function showGuideTip(owner){if(tooltipDismissed===owner)return;ensureHelpElements();clearTimeout(tooltipHideTimer);hideGuideTip();tooltipOwner=owner;const t=document.getElementById('guide-tooltip');t.textContent=owner.dataset.tip;t.hidden=false;owner.setAttribute('aria-describedby','guide-tooltip');const r=owner.getBoundingClientRect();let left=Math.max(12,Math.min(window.innerWidth-t.offsetWidth-12,r.left));let top=r.bottom+8;if(top+t.offsetHeight>window.innerHeight-12)top=Math.max(12,r.top-t.offsetHeight-8);t.style.left=left+'px';t.style.top=top+'px';}
function hideGuideTip(){const t=document.getElementById('guide-tooltip');if(t)t.hidden=true;if(tooltipOwner)tooltipOwner.removeAttribute('aria-describedby');tooltipOwner=null;}
function scheduleTipHide(){clearTimeout(tooltipHideTimer);tooltipHideTimer=setTimeout(()=>{const t=document.getElementById('guide-tooltip');if(t?.matches(':hover')||tooltipOwner?.matches(':hover')||document.activeElement===tooltipOwner)return;hideGuideTip();},140);}
function initHelp(){ensureHelpElements();const d=document.getElementById('help-dialog');d.addEventListener('close',()=>{if(helpReturnFocus?.isConnected)helpReturnFocus.focus({preventScroll:true});});d.addEventListener('click',e=>{if(e.target.closest('a[href^="#/"]')){closeGuideHelp();if(e.target.closest('a').getAttribute('href')===location.hash)route();}});
 document.addEventListener('click',e=>{const b=e.target.closest('[data-help]');if(b){e.preventDefault();openGuideHelp(b.dataset.help,b);}if(e.target.closest('[data-action="close-help"]'))closeGuideHelp();});
 document.addEventListener('pointerover',e=>{if(e.pointerType==='touch')return;const b=e.target.closest('[data-tip]');if(b)showGuideTip(b);if(e.target.closest('#guide-tooltip'))clearTimeout(tooltipHideTimer);});
 document.addEventListener('pointerout',e=>{if(e.target.closest('[data-tip]')){if(tooltipDismissed===e.target.closest('[data-tip]'))tooltipDismissed=null;scheduleTipHide();}if(e.target.closest('#guide-tooltip'))scheduleTipHide();});
 document.addEventListener('focusin',e=>{const b=e.target.closest('[data-tip]');if(b)showGuideTip(b);});document.addEventListener('focusout',e=>{if(e.target.closest('[data-tip]')){tooltipDismissed=null;scheduleTipHide();}});
 document.addEventListener('keydown',e=>{if(e.key==='Escape'&&tooltipOwner){tooltipDismissed=tooltipOwner;hideGuideTip();}});window.addEventListener('scroll',hideGuideTip,{passive:true});window.addEventListener('resize',hideGuideTip);}

