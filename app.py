import json
from flask import Flask, render_template_string

app = Flask(__name__)

# بيانات المحاضرات
lectures = [
    { "id": 1, "title": "Anatomy & physiology of ear", "doctor": "د.فؤاد شمسان", "links": [ { "label": "التقرير", "url": "https://t.me/september216thbatchENT/58", "type": 'report' }, { "label": "التسجيل", "url": "https://t.me/september216thbatchENT/56", "type": 'recording' }, { "label": "الملزمة", "url": "https://t.me/september216thbatchENT/55", "type": 'materials' } ] },
    { "id": 2, "title": "Symptomatology & examination of Ear", "doctor": "د.فؤاد شمسان", "links": [ { "label": "التقرير", "url": "https://t.me/september216thbatchENT/59", "type": 'report' }, { "label": "التسجيل", "url": "https://t.me/september216thbatchENT/57", "type": 'recording' }, { "label": "الملزمة", "url": "https://t.me/september216thbatchENT/55", "type": 'materials' } ] },
    { "id": 3, "title": "Otosclerosis & Facial nerve", "doctor": "د.حنان داؤود", "links": [ { "label": "التقرير", "url": "https://t.me/september216thbatchENT/75", "type": 'report' }, { "label": "التسجيل", "url": "https://t.me/september216thbatchENT/60", "type": 'recording' }, { "label": "الملزمة", "url": "https://t.me/september216thbatchENT/73", "type": 'materials' } ] },
    { "id": 4, "title": "Diseases of Inner ear & Nose", "doctor": "د.حنان داؤود", "links": [ { "label": "التقرير", "url": "https://t.me/september216thbatchENT/74", "type": 'report' }, { "label": "التسجيل", "url": "https://t.me/september216thbatchENT/62", "type": 'recording' }, { "label": "الملزمة", "url": "https://t.me/september216thbatchENT/73", "type": 'materials' } ] },
    { "id": 5, "title": "Diseases of External Ear", "doctor": "د. ضياء السروري", "links": [ { "label": "التقرير", "url": "https://t.me/september216thbatchENT/77", "type": 'report' }, { "label": "التسجيل", "url": "https://t.me/september216thbatchENT/63", "type": 'recording' }, { "label": "الملزمة", "url": "https://t.me/september216thbatchENT/78", "type": 'materials' } ] },
    { "id": 6, "title": "Acute Otitis media", "doctor": "د.زيد المراني", "links": [ { "label": "التقرير", "url": "https://t.me/september216thbatchENT/110", "type": 'report' }, { "label": "الملزمة", "url": "https://t.me/september216thbatchENT/101", "type": 'materials' } ] },
    { "id": 7, "title": "Anatomy of the larynx", "doctor": "د.خالد عثرب", "links": [ { "label": "التقرير", "url": "https://t.me/september216thbatchENT/87", "type": 'report' }, { "label": "التسجيل", "url": "https://t.me/september216thbatchENT/79", "type": 'recording' }, { "label": "الملزمة", "url": "https://t.me/september216thbatchENT/83", "type": 'materials' } ] },
    { "id": 8, "title": "Tracheostomy", "doctor": "د.خالد عثرب", "links": [ { "label": "التقرير", "url": "https://t.me/september216thbatchENT/88", "type": 'report' }, { "label": "التسجيل", "url": "https://t.me/september216thbatchENT/80", "type": 'recording' }, { "label": "الملزمة", "url": "https://t.me/september216thbatchENT/84", "type": 'materials' } ] },
    { "id": 9, "title": "Diseases of Larynx", "doctor": "د.سلوى الحمادي", "links": [ { "label": "التقرير", "url": "https://t.me/september216thbatchENT/89", "type": 'report' }, { "label": "التسجيل", "url": "https://t.me/september216thbatchENT/81", "type": 'recording' }, { "label": "الملزمة", "url": "https://t.me/september216thbatchENT/86", "type": 'materials' } ] },
    { "id": 10, "title": "Rhinosinusitis", "doctor": "د.نجلاء المقالح", "links": [ { "label": "التقرير", "url": "https://t.me/september216thbatchENT/91", "type": 'report' }, { "label": "التسجيل", "url": "https://t.me/september216thbatchENT/90", "type": 'recording' }, { "label": "الملزمة", "url": "https://t.me/september216thbatchENT/98", "type": 'materials' } ] }
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>فهرس ENT - جامعة 21 سبتمبر</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&display=swap" rel="stylesheet">
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        body { font-family: 'IBM Plex Sans Arabic', sans-serif; background-color: #F8FAFC; margin: 0; direction: rtl; }
        .header-fixed { position: sticky; top: 0; z-index: 50; background-color: rgba(248, 250, 252, 0.9); backdrop-filter: blur(8px); border-bottom: 2px solid #e2e8f0; }
        .flat-card { background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 1.5rem; transition: transform 0.2s; }
        .flat-card:hover { transform: translateY(-2px); border-color: #2D65FF; }
    </style>
</head>
<body>
    <div id="app">
        <header class="header-fixed px-6 py-5">
            <div class="max-w-xl mx-auto flex items-center gap-3 mb-5">
                <div class="w-10 h-10 bg-[#2D65FF] text-white rounded-xl flex items-center justify-center shadow-lg">
                    <i data-lucide="stethoscope" size="20"></i>
                </div>
                <div>
                    <h1 class="text-lg font-bold text-slate-800 leading-none">جامعة 21 سبتمبر</h1>
                    <p class="text-[9px] font-bold text-[#2D65FF] uppercase mt-1">فهرس ENT • الدفعة 6</p>
                </div>
            </div>
            <div class="max-w-xl mx-auto relative">
                <i data-lucide="search" class="absolute right-4 top-1/2 -translate-y-1/2 text-slate-400" size="18"></i>
                <input type="text" id="searchInput" placeholder="ابحث عن محاضرة..." class="w-full bg-white border-2 border-slate-200 rounded-xl py-3 pr-12 pl-4 text-sm outline-none focus:border-[#2D65FF]">
            </div>
        </header>

        <main class="max-w-xl mx-auto px-5 pt-8 pb-16">
            <div class="mb-8 p-6 bg-[#2D65FF] rounded-2xl text-white flex justify-between items-center shadow-xl">
                <div>
                    <h2 class="text-xl font-bold">كلية الطب البشري</h2>
                    <p class="text-xs font-bold opacity-90 uppercase">قسم الـ ENT - فهرس المحاضرات</p>
                </div>
                <i data-lucide="book-open" size="30"></i>
            </div>
            <div id="lectureList" class="space-y-6"></div>
        </main>
    </div>

    <script>
        const lectures = {{ lectures_json|safe }};
        const iconCfg = {
            report: { i: 'file-text', c: 'bg-emerald-50 text-emerald-600', l: 'تقرير' },
            recording: { i: 'mic', c: 'bg-indigo-50 text-indigo-600', l: 'تسجيل' },
            materials: { i: 'book-open', c: 'bg-blue-50 text-blue-600', l: 'ملزمة' },
            default: { i: 'folder', c: 'bg-slate-50 text-slate-500', l: 'محتوى' }
        };

        function render(list) {
            const container = document.getElementById('lectureList');
            container.innerHTML = list.map(l => `
                <div class="flat-card p-6 shadow-sm">
                    <div class="mb-4">
                        <span class="text-[9px] font-black bg-[#2D65FF] text-white px-2.5 py-1 rounded-lg mb-2 inline-block">محاضرة ${l.id}</span>
                        <h4 class="text-lg font-bold text-slate-800 leading-tight mb-1">${l.title}</h4>
                        <p class="text-[10px] text-slate-400 font-bold uppercase">د. ${l.doctor}</p>
                    </div>
                    <div class="grid grid-cols-2 gap-3">
                        ${l.links.map(link => {
                            const d = iconCfg[link.type] || iconCfg.default;
                            return `
                                <a href="${link.url}" target="_blank" class="flex items-center gap-3 p-3 rounded-xl bg-slate-50 border-2 border-slate-100 hover:border-blue-100 transition-all">
                                    <div class="w-8 h-8 rounded-lg flex items-center justify-center ${d.c} shrink-0">
                                        <i data-lucide="${d.i}" size="16"></i>
                                    </div>
                                    <div class="min-w-0">
                                        <span class="text-[8px] font-bold text-slate-400 block mb-0.5 uppercase">${d.l}</span>
                                        <span class="text-[11px] font-bold text-slate-700 truncate block">${link.label}</span>
                                    </div>
                                </a>
                            `;
                        }).join('')}
                    </div>
                </div>
            `).join('');
            lucide.createIcons();
        }

        render(lectures);
        document.getElementById('searchInput').addEventListener('input', (e) => {
            const q = e.target.value.toLowerCase();
            const filtered = lectures.filter(l => l.title.toLowerCase().includes(q) || l.doctor.includes(q));
            render(filtered);
        });
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, lectures_json=json.dumps(lectures))

if __name__ == "__main__":
    app.run(debug=True)
