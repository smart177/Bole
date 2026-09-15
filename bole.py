<!DOCTYPE html>
<html lang="am" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bole Bingo - Pro Gaming Hub</title>
    <style>
        /* የገጽ ከለር ቲማዎች (Dark & Light Themes) */
        :root[data-theme="dark"] {
            --bg-body: #090d16;
            --surface: #131b2e;
            --surface-card: #1a233a;
            --text-main: #f1f5f9;
            --text-muted: #94a3b8;
            --primary: #8b5cf6;
            --primary-hover: #7c3aed;
            --primary-light: rgba(139, 92, 246, 0.15);
            --border: #2a3650;
            --success: #10b981;
            --success-bg: rgba(16, 185, 129, 0.12);
            --danger: #ef4444;
            --danger-bg: rgba(239, 68, 68, 0.12);
            --shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.5);
        }

        :root[data-theme="light"] {
            --bg-body: #f8fafc;
            --surface: #ffffff;
            --surface-card: #ffffff;
            --text-main: #0f172a;
            --text-muted: #64748b;
            --primary: #7c3aed;
            --primary-hover: #6d28d9;
            --primary-light: rgba(124, 58, 237, 0.1);
            --border: #e2e8f0;
            --success: #059669;
            --success-bg: #d1fae5;
            --danger: #dc2626;
            --danger-bg: #fee2e2;
            --shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05);
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            transition: background-color 0.3s ease, border-color 0.3s ease, color 0.3s ease;
        }

        body {
            background: var(--bg-body);
            color: var(--text-main);
            font-family: 'Inter', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            text-align: center;
            padding-bottom: 100px;
            min-height: 100vh;
            -webkit-tap-highlight-color: transparent;
        }

        /* 10 ሰከንድ ሎዲንግ ስክሪን አኒሜሽን */
        #loader-wrapper {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: var(--bg-body);
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            z-index: 9999;
            transition: opacity 0.5s ease, visibility 0.5s ease;
        }
        .loader-logo {
            font-size: 32px;
            font-weight: 900;
            color: var(--primary);
            margin-bottom: 20px;
            letter-spacing: 2px;
            text-transform: uppercase;
            animation: pulseGlow 1.5s infinite;
        }
        .spinner {
            width: 50px;
            height: 50px;
            border: 4px solid var(--border);
            border-top: 4px solid var(--primary);
            border-radius: 50%;
            animation: spin 0.8s linear infinite;
        }
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        @keyframes pulseGlow {
            0% { opacity: 0.5; transform: scale(0.97); }
            50% { opacity: 1; transform: scale(1.03); }
            100% { opacity: 0.5; transform: scale(0.97); }
        }

        /* ፕሪሚየም ሄደር (Header with Night/Day Mode Toggle) */
        .app-header {
            padding: 16px 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: var(--surface);
            border-bottom: 1px solid var(--border);
            position: sticky;
            top: 0;
            z-index: 1000;
            box-shadow: var(--shadow);
        }
        .app-header h1 {
            color: var(--primary);
            font-size: 20px;
            font-weight: 800;
            letter-spacing: 1px;
        }

        .header-actions {
            display: flex;
            gap: 8px;
            align-items: center;
        }

        /* ናይት/ዳይ ሞድ መቀየሪያ ቁልፍ */
        .theme-toggle-btn, .auto-play-btn {
            background: var(--primary-light);
            color: var(--primary);
            border: 1px solid var(--border);
            padding: 7px 12px;
            border-radius: 10px;
            cursor: pointer;
            font-size: 13px;
            font-weight: 600;
            display: flex;
            align-items: center;
            gap: 5px;
        }
        .theme-toggle-btn:hover, .auto-play-btn:hover {
            background: var(--primary);
            color: #ffffff;
        }
        .auto-play-btn.active {
            background: var(--primary);
            color: #ffffff;
            box-shadow: 0 0 15px var(--primary-light);
        }

        /* ሒሳብ እና ምርጫ ማሳያ ባር */
        .game-top-bar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: var(--surface-card);
            margin: 16px;
            padding: 14px 20px;
            border-radius: 16px;
            border: 1px solid var(--border);
            box-shadow: var(--shadow);
        }
        .balance-info span {
            font-size: 11px;
            color: var(--text-muted);
            display: block;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        .balance-info strong {
            font-size: 18px;
            color: var(--primary);
            font-weight: 800;
        }

        /* የስታተስ ሣጥን */
        .status-box {
            background: var(--danger-bg);
            color: var(--danger);
            padding: 12px;
            border-radius: 12px;
            margin: 0 16px 16px 16px;
            font-weight: 600;
            font-size: 13px;
            border: 1px solid var(--border);
        }
        .status-box.active {
            background: var(--success-bg);
            color: var(--success);
        }

        /* የገጾች መዋቅር */
        .page-container {
            display: none;
            padding: 0 12px;
        }
        .page-container.active {
            display: block;
        }

        /* አዲስ የቢንጎ ሰሌዳ ዲዛይን */
        .bingo-grid {
            display: grid;
            grid-template-columns: repeat(10, 1fr);
            gap: 8px;
            max-width: 520px;
            width: 100%;
            margin: 0 auto;
            background: var(--surface-card);
            padding: 16px;
            border-radius: 20px;
            border: 1px solid var(--border);
            box-shadow: var(--shadow);
        }
        .bingo-cell {
            background: var(--bg-body);
            color: var(--text-main);
            font-weight: 700;
            font-size: 13px;
            aspect-ratio: 1;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 10px;
            cursor: pointer;
            border: 1px solid var(--border);
            user-select: none;
        }
        .bingo-cell:hover {
            border-color: var(--primary);
            transform: translateY(-2px);
        }
        .bingo-cell.selected {
            background: var(--primary);
            color: #ffffff;
            border-color: var(--primary);
            box-shadow: 0 0 12px var(--primary-light);
            transform: scale(1.05);
        }

        /* የካርድ ገጾች (Wallet, Rank, Profile) */
        .content-card {
            background: var(--surface-card);
            margin: 20px auto;
            padding: 30px;
            width: 90%;
            max-width: 400px;
            border-radius: 20px;
            border: 1px solid var(--border);
            box-shadow: var(--shadow);
            text-align: center;
        }
        .content-card h3 {
            color: var(--primary);
            margin-bottom: 12px;
            font-size: 20px;
        }

        /* ፖፕ-አፕ ሞዳል */
        .custom-modal {
            display: none;
            position: fixed;
            z-index: 2000;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.6);
            backdrop-filter: blur(5px);
            justify-content: center;
            align-items: center;
        }
        .modal-content {
            background: var(--surface-card);
            border: 1px solid var(--border);
            padding: 25px;
            border-radius: 20px;
            width: 85%;
            max-width: 320px;
            text-align: center;
            box-shadow: var(--shadow);
        }
        .modal-content p {
            color: var(--text-main);
            font-size: 15px;
            margin-bottom: 20px;
        }
        .modal-btn {
            background: var(--primary);
            color: #ffffff;
            border: none;
            padding: 10px 30px;
            font-weight: 700;
            border-radius: 10px;
            cursor: pointer;
        }

        /* የታችኛው ፉተር ሜኑ */
        .footer-nav {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background: var(--surface);
            display: flex;
            justify-content: space-around;
            padding: 12px 0;
            border-top: 1px solid var(--border);
            z-index: 1000;
            box-shadow: var(--shadow);
        }
        .nav-item {
            color: var(--text-muted);
            text-decoration: none;
            font-size: 11px;
            font-weight: 600;
            display: flex;
            flex-direction: column;
            align-items: center;
            cursor: pointer;
            flex: 1;
        }
        .nav-item.active {
            color: var(--primary);
        }
        .nav-item span {
            font-size: 20px;
            margin-bottom: 4px;
        }

        @media (max-width: 480px) {
            .bingo-grid { gap: 5px; padding: 10px; }
            .bingo-cell { font-size: 11px; border-radius: 8px; }
        }
    </style>
</head>
<body>

    <!-- 10 ሰከንድ ሎዲንግ አኒሜሽን ስክሪን -->
    <div id="loader-wrapper">
        <div class="loader-logo">Bole Pro</div>
        <div class="spinner"></div>
    </div>

    <!-- አዲስ የላይኛው ሄደር (ከ Night/Day Mode ቁልፍ ጋር) -->
    <header class="app-header">
        <h1>Bole Pro</h1>
        <div class="header-actions">
            <button class="theme-toggle-btn" onclick="toggleTheme()" id="themeBtn">🌙</button>
            <button id="autoPlayBtn" class="auto-play-btn" onclick="toggleAutoPlay()">
                <span id="autoIcon">🤖</span> <span id="autoText">Auto</span>
            </button>
        </div>
    </header>

    <!-- የሒሳብ እና ቆጣሪ ባር -->
    <section class="game-top-bar">
        <div class="balance-info">
            <span>Balance</span>
            <strong>50.00 ETB</strong>
        </div>
        <div style="font-size: 13px; color: var(--primary); font-weight: 700;">
            የተመረጡ: <span id="count">0</span> / 4
        </div>
    </section>

    <!-- የጨዋታ ሁኔታ ማሳያ -->
    <div id="gameStatus" class="status-box">Please wait, next game round</div>

    <!-- የቤት ገጽ (Bingo Grid) -->
    <main id="homePage" class="page-container active">
        <div class="bingo-grid" id="bingoGrid">
            <?php
            for ($i = 1; $i <= 120; $i++) {
                echo "<div class='bingo-cell' data-num='$i' onclick='selectCell(this)'>$i</div>";
            }
            ?>
        </div>
    </main>

    <!-- የኪስ ቦርሳ ገጽ -->
    <section id="walletPage" class="page-container">
        <div class="content-card">
            <h3>Wallet Balance</h3>
            <p style="font-size: 26px; font-weight: 800; margin: 15px 0; color: var(--success);">50.00 ETB</p>
            <p style="color: var(--text-muted); font-size: 13px;">Main Play Account</p>
        </div>
    </section>

    <!-- የደረጃ ገጽ -->
    <section id="rankPage" class="page-container">
        <div class="content-card">
            <h3>Leaderboard</h3>
            <p style="color: var(--text-muted); margin-top: 15px; font-size: 14px;">የተሸላሚዎች ዝርዝር በዚህ ይደረደራል...</p>
        </div>
    </section>

    <!-- የፕሮፋይል ገጽ -->
    <section id="profilePage" class="page-container">
        <div class="content-card">
            <h3>User Profile</h3>
            <p style="color: var(--text-muted); margin-top: 15px; font-size: 14px;">የመለያዎ መረጃዎች እና ቅንብሮች...</p>
        </div>
    </section>

    <!-- ፖፕ-አፕ ማሳወቂያ -->
    <div id="customModal" class="custom-modal">
        <div class="modal-content">
            <p id="modalMessage">ማሳወቂያ</p>
            <button class="modal-btn" onclick="closeModal()">OK</button>
        </div>
    </div>

    <!-- የታችኛው ናቪጌሽን ባር -->
    <nav class="footer-nav">
        <div class="nav-item active" onclick="switchPage('home', this)">
            <span>🏠</span> Home
        </div>
        <div class="nav-item" onclick="switchPage('wallet', this)">
            <span>💳</span> Wallet
        </div>
        <div class="nav-item" onclick="switchPage('rank', this)">
            <span>🏆</span> Rank
        </div>
        <div class="nav-item" onclick="switchPage('profile', this)">
            <span>👤</span> Profile
        </div>
    </nav>

    <script>
        // የ 10 ሰከንድ ሎዲንግ አኒሜሽን ስክሪፕት
        window.addEventListener('load', function() {
            setTimeout(function() {
                const loader = document.getElementById('loader-wrapper');
                loader.style.opacity = '0';
                loader.style.visibility = 'hidden';
            }, 10000); 
        });

        // Night / Day Mode Toggle Logic
        function toggleTheme() {
            const html = document.documentElement;
            const themeBtn = document.getElementById('themeBtn');
            if (html.getAttribute('data-theme') === 'dark') {
                html.setAttribute('data-theme', 'light');
                themeBtn.innerText = '☀️';
            } else {
                html.setAttribute('data-theme', 'dark');
                themeBtn.innerText = '🌙';
            }
        }

        let isRoundStarted = false;
        let isAutoPlayActive = false;

        function showCustomAlert(message) {
            document.getElementById('modalMessage').innerText = message;
            document.getElementById('customModal').style.display = 'flex';
        }

        function closeModal() {
            document.getElementById('customModal').style.display = 'none';
        }

        function toggleAutoPlay() {
            if (isRoundStarted) {
                showCustomAlert("Please wait, this round started!");
                return;
            }

            isAutoPlayActive = !isAutoPlayActive;
            const btn = document.getElementById('autoPlayBtn');
            const text = document.getElementById('autoText');
            const icon = document.getElementById('autoIcon');

            if (isAutoPlayActive) {
                btn.classList.add('active');
                text.innerText = "ON";
                icon.innerText = "⚡";

                document.querySelectorAll('.bingo-cell.selected').forEach(c => c.classList.remove('selected'));

                let selectedNumbers = [];
                while (selectedNumbers.length < 4) {
                    let randomNum = Math.floor(Math.random() * 120) + 1;
                    if (!selectedNumbers.includes(randomNum)) {
                        selectedNumbers.push(randomNum);
                    }
                }

                selectedNumbers.forEach(num => {
                    let cell = document.querySelector(`.bingo-cell[data-num='${num}']`);
                    if (cell) cell.classList.add('selected');
                });

                document.getElementById('count').innerText = "4";
            } else {
                btn.classList.remove('active');
                text.innerText = "Auto";
                icon.innerText = "🤖";

                document.querySelectorAll('.bingo-cell.selected').forEach(c => c.classList.remove('selected'));
                document.getElementById('count').innerText = "0";
            }
        }

        function selectCell(cell) {
            if (isRoundStarted) {
                showCustomAlert("Please wait, this round started!");
                return;
            }

            if (isAutoPlayActive) {
                showCustomAlert("እባክዎ መጀመሪያ Auto Mode ያጥፉ!");
                return;
            }

            cell.classList.toggle('selected');
            
            const selectedCells = document.querySelectorAll('.bingo-grid .bingo-cell.selected');
            const selectedCount = selectedCells.length;
            document.getElementById('count').innerText = selectedCount;
            
            if (selectedCount > 4) {
                showCustomAlert('ከ 4 በላይ ቁጥር መምረጥ አይችሉም!');
                cell.classList.remove('selected');
                document.getElementById('count').innerText = document.querySelectorAll('.bingo-grid .bingo-cell.selected').length;
            }
        }

        function switchPage(pageName, element) {
            document.querySelectorAll('.page-container').forEach(page => {
                page.classList.remove('active');
            });
            
            document.getElementById(pageName + 'Page').classList.add('active');

            document.querySelectorAll('.nav-item').forEach(item => {
                item.classList.remove('active');
            });
            element.classList.add('active');
        }

        function setGameRoundState(started) {
            isRoundStarted = started;
            const statusBox = document.getElementById('gameStatus');
            
            if (started) {
                statusBox.innerText = "Please wait, this round started!";
                statusBox.classList.add('active');
            } else {
                statusBox.innerText = "Please wait, next game round";
                statusBox.classList.remove('active');
            }
        }
    </script>
</body>
</html>
