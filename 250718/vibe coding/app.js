// 채팅 전송 및 수신을 위한 선택
const chatInput = document.querySelector('.chat-input')
// const chatSubmitIcon = document.querySelector('.chat-submit-icon')
const chatContainer = document.querySelector('.chat-area')

// 채팅창에 내용을 추가해주는 부분
const addChat = (type, value) => {
  const chat = document.createElement('div')
  chat.classList.add('chat')
  chat.innerText = value
  chat.classList.add(`${type}-chat`)
  chatContainer.appendChild(chat)
  chatContainer.scrollTop = chatContainer.scrollHeight
}

// 1. 챗봇 서버에 요청할 URL (chatGPT API reference Chat 파트 참고)
const OPEN_API_URL = 'https://api.openai.com/v1/chat/completions'
// 2. API 키 (발급 받은 Secret Key)
const API_KEY = ''

// 필요한 헤더 정보
const headers = {
  Authorization: `Bearer ${API_KEY}`, // 인증 키 설정
  'Content-Type': 'application/json' // 요청 데이터의 타입
}

// 이전에 응답받은 메세지를 저장하는 변수
let oldMsg = ''

// 모든 대화를 저장하는 배열
let messages = []

// 타이핑 효과로 텍스트 출력
function typeText(type, text) {
  const chat = document.createElement('div');
  chat.classList.add('chat', `${type}-chat`);
  chatContainer.appendChild(chat);
  chatContainer.scrollTop = chatContainer.scrollHeight;
  let i = 0;
  function typing() {
    if (i <= text.length) {
      chat.innerText = text.slice(0, i);
      chatContainer.scrollTop = chatContainer.scrollHeight;
      i++;
      setTimeout(typing, 20);
    }
  }
  typing();
}

const chatReceive = (userMsg) => {
  messages.push({ role: 'user', content: userMsg });
  axios({
    method: 'post',
    url: OPEN_API_URL,
    headers,
    data: {
      model: 'gpt-4o-mini',
      messages: messages
    }
  })
    .then(res => {
      console.log(res.data);
      const response = res.data.choices[0].message.content;
      typeText('receive', response);
      messages.push({ role: 'assistant', content: response });
    })
    .catch(err => {
      console.log(err.response.data);
      console.log(err.response.status);
    });
}
axios({
  method: 'post',
  url: OPEN_API_URL,
  headers,
  data: {
    model: 'gpt-4o-mini',
    messages
  }
})
  .then(res => {
    console.log(res.data);
    const response = res.data.choices[0].message.content;
    // 타이핑 효과로 출력
    typeText('receive', response);
    // 챗봇 응답도 messages 배열에 추가
    messages.push({ role: 'assistant', content: response });
  })
  .catch(err => {
    console.log(err.response.data);
    console.log(err.response.status);
  });

const chatSubmit = () => {
  const value = chatInput.value
  if (!value) return
  addChat('send', value)
  chatReceive(value)
  chatInput.value = ''
}


chatInput.addEventListener('keyup', (e) => {
  e.key === 'Enter' && chatSubmit()
})
