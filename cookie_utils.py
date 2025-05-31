# cookie_utils.py
import streamlit as st
import json
import base64
from datetime import date

def serialize_for_cookie(data):
    """序列化数据用于cookie存储"""
    if isinstance(data, dict):
        serialized = {}
        for key, value in data.items():
            if isinstance(value, date):
                serialized[key] = value.isoformat()
            elif value is None:
                serialized[key] = None
            else:
                serialized[key] = value
        return serialized
    return data

def deserialize_from_cookie(data):
    """从cookie反序列化数据"""
    if isinstance(data, dict):
        deserialized = {}
        for key, value in data.items():
            if key == 'birthday' and isinstance(value, str):
                try:
                    deserialized[key] = date.fromisoformat(value)
                except:
                    deserialized[key] = date(2019, 5, 15)  # 默认日期
            else:
                deserialized[key] = value
        return deserialized
    return data

def save_profile_to_cookie(profile_data):
    """保存profile到cookie"""
    try:
        # 序列化数据
        serialized_data = serialize_for_cookie(profile_data)
        json_str = json.dumps(serialized_data)
        
        # Base64编码以处理特殊字符
        encoded_data = base64.b64encode(json_str.encode('utf-8')).decode('utf-8')
        
        # 使用JavaScript设置cookie
        cookie_script = f"""
        <script>
        try {{
            // 设置cookie，30天过期
            const expirationDate = new Date();
            expirationDate.setTime(expirationDate.getTime() + (30 * 24 * 60 * 60 * 1000));
            document.cookie = "meowmatch_profile={encoded_data}; expires=" + expirationDate.toUTCString() + "; path=/; SameSite=Lax";
            
            console.log('✅ Profile saved to cookie successfully');
            
            // 设置一个标志表示保存成功
            sessionStorage.setItem('cookie_save_status', 'success');
        }} catch (error) {{
            console.error('❌ Error saving profile to cookie:', error);
            sessionStorage.setItem('cookie_save_status', 'error');
        }}
        </script>
        """
        
        # 使用Streamlit的HTML组件执行JavaScript
        st.components.v1.html(cookie_script, height=0)
        return True
        
    except Exception as e:
        st.error(f"保存配置文件失败: {e}")
        return False

def get_cookie_data():
    """获取cookie数据的JavaScript函数"""
    cookie_reader_script = """
    <script>
    function getCookie(name) {
        const value = "; " + document.cookie;
        const parts = value.split("; " + name + "=");
        if (parts.length === 2) {
            return parts.pop().split(";").shift();
        }
        return null;
    }
    
    try {
        const profileCookie = getCookie('meowmatch_profile');
        if (profileCookie) {
            // 解码Base64数据
            const decodedData = atob(profileCookie);
            const profileData = JSON.parse(decodedData);
            
            // 将数据存储到sessionStorage以便Streamlit访问
            sessionStorage.setItem('meowmatch_temp_profile', JSON.stringify(profileData));
            console.log('✅ Profile loaded from cookie');
        } else {
            console.log('ℹ️ No profile cookie found');
            sessionStorage.removeItem('meowmatch_temp_profile');
        }
    } catch (error) {
        console.error('❌ Error reading profile cookie:', error);
        sessionStorage.removeItem('meowmatch_temp_profile');
    }
    </script>
    """
    
    st.components.v1.html(cookie_reader_script, height=0)

def load_profile_from_cookie():
    """从cookie加载profile数据"""
    # 首先执行JavaScript来读取cookie
    get_cookie_data()
    
    # 检查是否有URL参数传递的数据（备用方法）
    query_params = st.experimental_get_query_params()
    if 'profile' in query_params:
        try:
            encoded_profile = query_params['profile'][0]
            decoded_data = base64.b64decode(encoded_profile.encode('utf-8')).decode('utf-8')
            profile_data = json.loads(decoded_data)
            return deserialize_from_cookie(profile_data)
        except Exception as e:
            st.warning(f"无法从URL参数加载配置文件: {e}")
    
    return None

def clear_profile_cookie():
    """清除profile cookie"""
    clear_script = """
    <script>
    try {
        document.cookie = "meowmatch_profile=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/; SameSite=Lax";
        sessionStorage.removeItem('meowmatch_temp_profile');
        console.log('✅ Profile cookie cleared');
    } catch (error) {
        console.error('❌ Error clearing cookie:', error);
    }
    </script>
    """
    st.components.v1.html(clear_script, height=0)

def check_cookie_support():
    """检查浏览器是否支持cookie"""
    check_script = """
    <script>
    try {
        // 测试设置一个临时cookie
        document.cookie = "test_cookie=1; path=/; SameSite=Lax";
        const cookieEnabled = document.cookie.indexOf("test_cookie=") !== -1;
        
        // 清除测试cookie
        document.cookie = "test_cookie=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/; SameSite=Lax";
        
        sessionStorage.setItem('cookie_support', cookieEnabled ? 'true' : 'false');
        console.log('Cookie support:', cookieEnabled);
    } catch (error) {
        sessionStorage.setItem('cookie_support', 'false');
        console.error('Cookie support check failed:', error);
    }
    </script>
    """
    st.components.v1.html(check_script, height=0)

# 默认配置文件数据
DEFAULT_PROFILE = {
    'pet_name': '🐱',
    'breed': '',
    'gender': '',
    'age': 0,
    'weight': 0,
    'birthday': date(2025, 6, 6),
    'activity_level': 'Moderate',
    'favorite_flavors': [],
    'allergies': [],
    'health_conditions': [],
    'special_notes': '',
    'profile_image': None,
    'profile_image_base64': None
}