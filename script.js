const fs = require('fs');

// 读取JSON文件
function readStatusData() {
    try {
        const data = fs.readFileSync('./status_data.json', 'utf8');
        return JSON.parse(data);
    } catch (err) {
        console.error('读取状态数据文件时出错:', err);
        return { days: [1], current: 1 }; // 返回默认值
    }
}

document.addEventListener('DOMContentLoaded', function() {
    const statusData = readStatusData();
    
    // 更新当前状态显示
    const statusText = document.getElementById('status-text');
    if (statusData.current === 1) {
        statusText.textContent = '正常';
    } else if (statusData.current === 2) {
        statusText.textContent = '不正常';
    } else if (statusData.current === 3) {
        statusText.textContent = '已恢复正常';
    }

    // 更新状态网格
    const grid = document.getElementById('status-grid');
    grid.innerHTML = ''; // 清空现有网格
    statusData.days.forEach(day => {
        const box = document.createElement('div');
        box.classList.add('status-box');
        if (day === 1) box.classList.add('green');
        else if (day === 2) box.classList.add('red');
        else if (day === 3) box.classList.add('yellow');
        grid.appendChild(box);
    });
});