import streamlit as st
import random
import time
import base64
st.title("funny")
tabroblox,tabfacebook,tabmessanger,tabhelp,brử_skibidi_dom_dom_dom_yes_yes_skibidi_double_ron_li_li_skibidi_dom_dom_dom_yes_yes_skibidi_double_ron_li_li=st.tabs(["roblox","facebook","messanger","help","entertainment games"])
with tabroblox:
    def play_click_sound(file_path):
        try:
            with open(file_path, "rb") as f:
                data = f.read()
                b64 = base64.b64encode(data).decode()
                
                # Đoạn HTML ẩn để tự động phát
                md = f"""
                    <audio autoplay style="display:none;">
                        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
                    </audio>
                    """
                st.markdown(md, unsafe_allow_html=True)
        except FileNotFoundError:
            st.error(f"Không tìm thấy file: {file_path}")
    play_click_sound("Mouse Click Sound Effect.mp3")
    st.header("roblox.com")
    st.title("play other game or make your own to let another play it")
with tabfacebook:
    st.header("facebook.com")
    st.title("chating, friends, watching other videos, read another post or you can make your own")
with tabmessanger:
    st.header("messanger.com")
    st.title("chating or friends...only that")
with tabhelp:
    st.header("🔮 Health")
    tabA, tabB, tabC, tabD, tabblaherror, tabblahbroke, tabblahbroken, tabblaherroR, = st.tabs(['BMI.com', 'heartrate.com','height.com','drink.com',"ERrOr","ERrOr","ERrOr","ERrOr",])
    with tabA:
        st.title("bmi")
        weight=st.number_input("YoUr WeIgHt(kg):",min_value=10.0,max_value=1000.0,value=60.0,step=1.0)
        height=st.number_input("YoUr HeIgHt(Meter):",min_value=0.4,max_value=2.5,value=1.7,step=0.01)
        bmi=weight/height**2
        if st.button("bmi"):
            st.success(f"Ok bmi:{bmi:.2f}")
            if bmi<18.5:
                st.warning("you're skinny")
            elif 18.4<bmi<24.9:
                st.info("yo bro your weight is normal")
            elif bmi>25:
                st.warning("you're overweight")
            elif 25<bmi<30:
                st.warning("the token of obesity")
            elif 30<bmi<34.9:
                st.warning("obesity level1")
            elif 34.9<bmi<40.1:
                st.warning("obesity level2")
            elif bmi>40:
                st.warning("obesity level3")
            else:
                st.error("you write wrong but..... HOW CAN YOU WRITE WRONG... THIS CANT BE TRUE")
    with tabB:
        st.title("safe heartrate")
        age=st.number_input("YoUr AgE:",min_value=0.0,max_value=130.0,value=18.0,step=1.0)
        heartrate=st.number_input("YoUr HeArTrAtE(bpm):",min_value=0.0,max_value=200.0,value=80.0,step=1.0)
        if st.button("heart"):
            if age<=1 and heartrate<100 or heartrate>160:
                st.warning("your baby heartrate is not safe")
            elif 1<age<11 and heartrate<70 or heartrate>120:
                st.warning("your heartrate is not safe")
            elif 10<=age<=64 and heartrate<60 or heartrate>100:
                st.warning("your heartrate is not safe")
            elif age>65 and heartrate<50 or heartrate>100:
                st.warning("your heartrate is not safe")
            elif age<=1 and 100<=heartrate<=160:
                st.info("your baby heartrate is normal")
            elif 1<age<11 and 70<=heartrate<=120:
                st.info("your heartrate is normal")
            elif 10<age<64 and 60<=heartrate<=100:
                st.info("your heartrate is normal")
            elif age>65 and 50<=heartrate<=100:
                st.info("your heartrate is normal")
            else:
                st.error("you write wrong but..... HOW CAN YOU WRITE WRONG... THIS CANT BE TRUE")
    with tabC:
        st.header("test4.com")
        st.title("normal height")
        height=st.number_input("YoUr HeIgHt(meter):",min_value=1.0,max_value=8.0,value=2.0,step=0.01)
        age4=st.number_input("YoUr AgE:",min_value=0.0,max_value=130.0,value=18.0,step=1.0, key="abc1")
        if st.button("sure?"):
            if age4<1 and height<0.40:
                st.warning("your baby height is shorter than the normal height")  
            elif age4==1 and height<0.65:
                st.warning("your baby height is shorter than the normal height")
            elif 1<age<=2 and height<0.75:
                st.warning("your baby height is shorter than the normal height")
            elif 2<age<=3 and height<0.85:
                st.warning("your baby height is shorter than the normal height")
            elif 3<age<=4 and height<0.9:
                st.warning("your baby height is shorter than the normal height")
            elif 4<age<=5 and height<1.0:
                st.warning("your baby height is shorter than the normal height")
            elif 5<age<=7 and height<1.05:
                st.warning("your baby height is shorter than the normal height")
            elif 7<age<=10 and height<1.3:
                st.warning("your height is shorter than the normal height")
            elif 10<age<=13 and height<1.4:
                st.warning("your height is shorter than the normal height")
            elif 13<age<=16 and height<1.5:
                st.warning("your height is shorter than the normal height")
            elif age4>16 and height<1.6:
                st.warning("your height is shorter than the normal height")
            elif age4<1 and height>0.50:
                st.info("your baby height is taller than the normal height")  
            elif age4==1 and height>0.85:
                st.info("your baby height is taller than the normal height")
            elif 1<age<=2 and height>0.95:
                st.info("your baby height is taller than the normal height")
            elif 2<age<=3 and height>1.0:
                st.info("your baby height is taller than the normal height")
            elif 3<age<=4 and height>1.05:
                st.info("your baby height is taller than the normal height")
            elif 4<age<=5 and height>1.1:
                st.info("your baby height is taller than the normal height")
            elif 5<age<=7 and height>1.3:
                st.info("your baby height is tallerr than the normal height")
            elif 7<age<=10 and height>1.4:
                st.info("your height is taller than the normal height")
            elif 10<age<=13 and height>1.5:
                st.info("your height is taller than the normal height")
            elif 13<age<=16 and height>1.7:
                st.info("your height is taller than the normal height")
            elif age4>16 and height>1.8:
                st.info("your height is taller than the normal height")
            elif age4>=17 and height==1.9:
                st.info("your height is equal Gojo Satoru height (just search jujutsu kaisen)")
            elif age4<1 and 0.40<=height<=0.50:
                st.info("your baby height is normal")  
            elif age4==1 and 0.65<=height<=0.85:
                st.info("your baby height is normal")
            elif 1<age<=2 and 0.75<=height<=0.95:
                st.info("your baby height is normal")
            elif 2<age<=3 and 0.85<=height<=1:
                st.info("your baby height is normal")
            elif 3<age<=4 and 0.9<=height<=1.05:
                st.info("your baby height is normal")
            elif 4<age<=5 and 1<=height<=1.1:
                st.info("your baby height is normal")
            elif 5<age<=7 and 1.05<=height<=1.3:
                st.info("your baby height is normal")
            elif 7<age<=10 and 1.3<=height<=1.4:
                st.info("your height is normal")
            elif 10<age<=13 and 1.4<=height<=1.5:
                st.info("your height is normal")
            elif 13<age<=16 and 1.5<=height<=1.7:
                st.info("your height is normal")
            elif age4>16 and 1.6<=height<=1.8:
                st.info("your height is normal")    
    with tabD:
        st.header("test3.com")
        st.title("safe liter of water per day")
        drink=st.number_input("YoUr DrInK pEr DaY(liter):",min_value=1.0,max_value=8.0,value=2.0,step=1.0)
        age3=int(st.number_input("YoUr AgE:",min_value=0.0,max_value=130.0,value=18.0,step=1.0,key="age_drink"))
        if st.button("drink"):
            if age3<=3 and drink<1.2 or drink>1.4:
                st.warning("your baby is drink not safe value of liter water per day")
            elif 3<age3<9 and drink<1.6 or drink>1.8:
                st.warning("you are drink not safe value of liter water per day")
            elif 9<=age3<=13 and drink<=2.1 or drink>=2.4:
                st.warning("you are drink not safe value of liter water per day")
            elif 14<=age3<=18 and drink<2.3 or drink>3.3:
                st.warning("you are drink not safe value of liter water per day")
            elif 19<=age3<=50 and drink<2.7 or drink>3.7:
                st.warning("you are drink not safe value of liter water per day")
            elif age3>50 and drink<2.5 or drink>3.0:
                st.warning("you are drink not safe value of liter water per day")
            elif age3<=3 and 1.2<=drink<=1.4:
                st.warning("your baby is drink normal value of liter water per day")
            elif 3<age3<9 and 1.6<=drink<=1.8:
                st.warning("you are drink normal value of liter water per day")
            elif 9<=age3<=13 and 2.1<=drink<=2.4:
                st.warning("you are drink normal value of liter water per day")
            elif 14<=age3<=18 and 2.3<=drink<=3.3:
                st.warning("you are drink normal value of liter water per day")
            elif 19<=age3<=50 and 2.7<=drink<=3.7:
                st.warning("you are drink normal value of liter water per day")
            elif age3>50 and 2.5<=drink<=3:
                st.warning("you are drink normal value of liter water per day")
            else:
                st.error("you write wrong but..... HOW CAN YOU WRITE WRONG... THIS CANT BE TRUE")
with tabblaherror:
    st.error("ErRoR")
    st.error("""2025-11-23 10:14:57.123 Uncaught app exception
Traceback (most recent call last):
  File "D:\Projects\myapp\?pp.py", line 42, in <module>
    main()
  File "D:\Projects\myapp\?pp.py", line 21, in main
    result = process_data(user_input)
  File "D:\Projects\myapp\?tils.py", line 77, in process_data
    cleaned = clean_text(text)
  File "D:\Projects\myapp\?tils.py", line 33, in clean_text
    return text.strip().lower()
AttributeError: 'NoneType' object has no attribute 'strip'

Streamlit encountered an error while running your script.

❌ **Error type:** AttributeError  
❌ **Message:** `'NoneType' object has no attribute 'strip'`

Traceback:
- File *app.py*, line 21, in *main*
- File *utils.py*, line 77, in *process_data*
- File *utils.py*, line 33, in *clean_text*

If you think this is a Streamlit bug, please file a report at:  
https://github.com/streamlit/streamlit/issues
""")
with tabblahbroke:
    st.error("ErRoR")
    st.error("""2025-11-23 10:14:57.123 Uncaught app exception
Traceback (most recent call last):
  File "D:\Projects\myapp\?pp.py", line 42, in <module>
    main()
  File "D:\Projects\myapp\?pp.py", line 21, in main
    result = process_data(user_input)
  File "D:\Projects\myapp\?tils.py", line 77, in process_data
    cleaned = clean_text(text)
  File "D:\Projects\myapp\?tils.py", line 33, in clean_text
    return text.strip().lower()
AttributeError: 'NoneType' object has no attribute 'strip'

Streamlit encountered an error while running your script.

❌ **Error type:** AttributeError  
❌ **Message:** `'NoneType' object has no attribute 'strip'`

Traceback:
- File *app.py*, line 21, in *main*
- File *utils.py*, line 77, in *process_data*
- File *utils.py*, line 33, in *clean_text*

If you think this is a Streamlit bug, please file a report at:  
https://github.com/streamlit/streamlit/issues
""")
with tabblahbroken:
    st.error("ErRoR")
    st.error("""2025-11-23 10:14:57.123 Uncaught app exception
Traceback (most recent call last):
  File "D:\Projects\myapp\?pp.py", line 42, in <module>
    main()
  File "D:\Projects\myapp\?pp.py", line 21, in main
    result = process_data(user_input)
  File "D:\Projects\myapp\?tils.py", line 77, in process_data
    cleaned = clean_text(text)
  File "D:\Projects\myapp\?tils.py", line 33, in clean_text
    return text.strip().lower()
AttributeError: 'NoneType' object has no attribute 'strip'

Streamlit encountered an error while running your script.

❌ **Error type:** AttributeError  
❌ **Message:** `'NoneType' object has no attribute 'strip'`

Traceback:
- File *app.py*, line 21, in *main*
- File *utils.py*, line 77, in *process_data*
- File *utils.py*, line 33, in *clean_text*

If you think this is a Streamlit bug, please file a report at:  
https://github.com/streamlit/streamlit/issues
""")
with tabblaherroR:
    st.error("ErRoR")
    st.error("""2025-11-23 10:14:57.123 Uncaught app exception
Traceback (most recent call last):
  File "D:\Projects\myapp\?pp.py", line 42, in <module>
    main()
  File "D:\Projects\myapp\?pp.py", line 21, in main
    result = process_data(user_input)
  File "D:\Projects\myapp\?tils.py", line 77, in process_data
    cleaned = clean_text(text)
  File "D:\Projects\myapp\?tils.py", line 33, in clean_text
    return text.strip().lower()
AttributeError: 'NoneType' object has no attribute 'strip'

Streamlit encountered an error while running your script.

❌ **Error type:** AttributeError  
❌ **Message:** `'NoneType' object has no attribute 'strip'`

Traceback:
- File *app.py*, line 21, in *main*
- File *utils.py*, line 77, in *process_data*
- File *utils.py*, line 33, in *clean_text*

If you think this is a Streamlit bug, please file a report at:  
https://github.com/streamlit/streamlit/issues
""")
with brử_skibidi_dom_dom_dom_yes_yes_skibidi_double_ron_li_li_skibidi_dom_dom_dom_yes_yes_skibidi_double_ron_li_li:
    tabA,tabB,tabC,tabD,tabE,tabbleo= st.tabs(['Scary game','Guess game','Rock Paper Scissors game...','ERROR','nothing','lucky game'])
    with st.sidebar:
        st.video("https://www.youtube.com/watch?v=ONya1v2cQvw")    
    with tabA:
        anxiety=0
        anxietybar=st.slider(f"Anxiety:{anxiety}/100", min_value=0,max_value=100)
        steps=0
        anxiety_steps=0  
        if steps==0:
            st.title("You are an security guard")
            time.sleep(2)
            st.subheader("You are in you room, sleeping")
            time.sleep(2)
            st.subheader("You're feeling terrible")
            time.sleep(2)
            st.subheader("You're feeling that someone is coming")
            time.sleep(2)
            st.subheader("You choose watch the camera")
            st.spinner("connecting to camera 9")
            time.sleep(5)
            st.title("SOMEONEISCOMINGSOMEONEISCOMINGSOMEONEISCOMINGSOMEONEISCOMINGSOMEONEISCOMINGSOMEONEISCOMINGSOMEONEISCOMINGSOMEONEISCOMINGSOMEONEISCOMINGSOMEONEISCOMINGSOMEONEISCOMINGSOMEONEISCOMINGSOMEONEISCOMINGSOMEONEISCOMINGSOMEONEISCOMING")
            if st.button("Hide?"):
                st.spinner("Hiding...")
                time.sleep(1.5)
                st.header("He entered the room...")
                st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQu8KiBqmj80kN5NGITNJQlYsW_a-0WZpo_Og&s")
                time.sleep(7)
                st.subheader("he left...")
                st.subheader("Now you need to watch camera to hold the creature in your eyes")
                steps+=1
            if st.button("stay still"):
                steps=3
            if steps==1:
                anxiety_steps=1
                if anxiety_steps==1:
                    anxiety+=1
                    anxiety_steps=0
                    time.sleep(1)
                    anxiety_steps+=1
                if st.button("watch camera?"):
                    steps+=2
            if steps==2:
                if st.button("camera 1"):
                    st.image
                


    with tabB:
        st.header("Guess game")
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT1vaP-RdkmVDRKTOVYKDxEh1HEDWfHEMR6uvIIbb_EMg&s")
        if "secret" not in st.session_state:
            st.session_state.secret = random.randint(1, 10000)
            st.session_state.tries = 0
        guess = st.number_input("Guess number from 1-10000 ", min_value = 1, max_value=10000, step = 1)
        if guess==st.session_state.secret:
            st.success(f"CONGRATULATIONS ! YOU GUESS RIGHT AFTER {st.session_state.tries} TIMES.")
            st.text('click the button "play again"')
            st.image("https://i.pinimg.com/736x/56/ec/c4/56ecc46e4afcd3e9c3a3ae2237cba59a.jpg")
            if st.button("play again"):
                st.session_state.secret=random.randint(1, 10000)
                st.session_state.tries=0     
        else:
            if st.button("Sure?"):
                st.session_state.truthorlie = random.randint(0,1)
                st.session_state.tries +=1
                if guess < st.session_state.secret:
                    if st.session_state.truthorlie==0:
                        st.info("more")
                    if st.session_state.truthorlie==1:
                        st.error("less")
                elif guess > st.session_state.secret:
                    if st.session_state.truthorlie==0:
                        st.warning("less")
                    if st.session_state.truthorlie==1:
                        st.error("more")
    with tabC:
        st.header("Rock Paper Scissors game...")
        time.sleep(2)
        st.spinner("Loading Computer")
        st.image("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAS4AAACnCAMAAACYVkHVAAAAwFBMVEUAAAAAzP8ULj4Azf0By/8AAAIuvuYnqckMP1sDAAA0wOwAy/wAER41vN0AzPofX3sAEhs0xe0CAAYAAwAGFiAPRFURXnYbepYjkq0mp8NNsM4YKjQAChQYS18XZH0olLQqstYCIy8bQE02jagAAAsgqM4muuUwyO02vtohXX4AzPUABhRTuNU1wudIv+ctW3IMNkgMQV0NQFYAGykMNFBDpcIYUmQueY8NJjY3NzdaWlqAgICVlZVHR0e3t7caGhqVrXpTAAADDklEQVR4nO3cjU/aQBjHcY67Au3BSesEp2y+DdEqm/iyOV+2//+/2nNt0ZaJ02RLJft+omhJSC6/PPf02l5oNAAAAAAAAAAAAAAAAAAAALB6wrB0ECSJPw5qG83bF2Tkjz9YX8/eqXlIb1klmzCQAqtrJKsgzGZfwYeXJMF63YN6o4LHnAqJ5BWEz3zkP+arqYgmeNfcGAw3329t0+ifNWp++Djcae+2Yue0i5rEVSEzL6+oYE9y2j/YbUVOOaWUkV/barKOWPDpYn8w3BkfxnE8WWs7Z5XSquDjonWVjbZiY62zRjuXSlw+K+Jaqn8kk08oq6xba5tiHj7ExYmxQuKSrIwyEpLEZX1clriW6beM0cpqq5WRuJz/RxPXMt2epOVn4jyu8mzkzLio2zIuWzho5Vu98bU2ly8kKK+S7pHTRTUZc9y2Pi4zF1FdC/pHNpuMkpG2x7KQkM5VnoxhSF4lo56Vpamsu6xL07WxFcrZnMsmI3GVnJxG0yiKWlEUR5+/XEXeNMpNT/0lNr2rZHR22ZnNzs87nVmnc9GUl9lMXnKXI+KqOjmdTuNYfqJ4KtUVTybZUWYi1RVyZizr96ycGaVh+V4lq3rpW6ZoXdlCgk5f4Zep84WEj0svXAShIl/V+zXpY1yauJbJ49LluFSlupiMZX+MC2VPxEXvWo5W/yr9I2eyi2zjjFwzSlTztIwy2UKCx7IlJ1uxTVO5bjTOZdWlpdqsT0xrO23mz7UxlyTds6/Dg3Evim0scaWpS10xF1OJK6C6yh7C2NsYfPPPGWPrjLb+3r2xh/SuqsBv4SpdRo+uzwfDzfHuYexkivLg7HdBkuT7SMLwYXdS93rf75G42uZ+1wJJSuIK8w1KQbap67GgkkbAHYkn+d0SWVw+MX8U5O8SFwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADg3/t+c3tX9xhWyP1t3SNYJXc3/pVv63o5snq5Hzd1j2CFBI2fdQ9hhWTfMPij7lGslvu6B7BK6POvwjd+AgAAAAAAAAAAAACAv+wX/8Iq+eaWWa8AAAAASUVORK5CYII=")
        time.sleep(2)
        st.image("data:image/jpeg;base64,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")
        st.image("data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxITEhUSEhIVFRUWGBUVFxcWFRcWFRUVGBYWFhUYFxUYHSggGBolHRUVITEhJSkrLi4uFx8zODMtNygtLisBCgoKDg0OGhAQGC8lHyUtLS0tLS0tLS0tLS0tLi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLf/AABEIAKgBKwMBEQACEQEDEQH/xAAcAAABBAMBAAAAAAAAAAAAAAAEAgMFBgABBwj/xABEEAACAQIDBAYHBQcCBQUAAAABAgMAEQQSIQUxQVEGEyJhcZEyQlKBobHBBxQjYnIVQ4KSstHwM+EWY4OiowgkJVNz/8QAGwEAAgMBAQEAAAAAAAAAAAAAAAECAwQFBgf/xAAzEQACAQIEAgcIAgMBAAAAAAAAAQIDEQQSITFBUQUTIjJhcZFCgaGxwdHh8CMzFFLxcv/aAAwDAQACEQMRAD8AogqwrIHbp7beCfSoMmtiOQdk+I+RoGZakAZsbZMmJmSCFbu5sOQHFmPBQLk+FV1qsaUHOWyBK56X6LdH4cFh0w8Q3as1tZHPpOe829wAHCvIYivKvUc5f8RelYlmjqgYHhMQkqCSM5lN7GxF7EqbX4XB141KcHB2YGSR1W0MrHSjonhsYPxUs4FlkXSReWvrDuN604bG1cO+y9OXAi4pnJNvdDp8E2Z4uvh9tGKgfrXUp8u+vS4XpClX0Wj5P6cyqUGgfAbWSO9oGAPIqbfHWt1yJIjpDEd6yL4ofpencB1Nt4c/vLfqDL8xTuIdj2hCd0qfzCmAQk4O4g+BpAAbZwQlTT0hqO/uoAqLrY2O/lSARagYVhpCNx10seRBBGnupAbxTEksRa+um7lp5UATGzrZACaACTAh3qp8QKQxP3GM+rbwJX5GmIScEvBnH8V/6r0AYIHG6VveAf6bUXCwtevHrqfcR8707sVkKXEzDeinwa/zAozCyi12iw9KJh5H+kmnmDKPYfaKsSAr3AJPYYaDedQNKMyBU5S2Fw7Sibc487/KndEcrCVmXmPOncLDgNAjdMDYoA2KANikBlMCvikMr+3D22/hFQZNAC+j/EfkP70hmCgDvv2XdD/uUPXTKPvMo7XOKPeI/HcW77DhXl+kcX108se6vi+f2LoxsXtTXOJEZ0qklGFkECO8jZUAjtnCuwV2W+lwpYi/ECtGHUXUWZ6eImI6NY4SK8IwzYf7uUiEbMjWXq1ZAMhIHZK6UV6eVqWa99b+/wAQRJNlJygi++1xe3O1Z3F7jBpo6raGAzR0tgKP0h6CRSXfD2iffl/dsfAegfDTursYXpadPs1dVz4/khKnfYoOO2ZLA+SVCrd+4jmDuI8K79KvCrHNB3RU00NiOrRGNhlO9QfcKAGzs+P2B5W+VFwMGEA3M48HYfWncBuXBlt7sfGzfEii4DDbMPB/NR9KLgJOzZODL5EU7gbOEm9lT4N/cUrgE4WSRBZoWPeCD9adwCk2iB6SSL4oT8qQC/2pD7dvEEfMUwHo8ZEd0in+IUAPqwO4g+FAChQM3akBtYixCqCSdABvJpjUXJ2RctlbFEKG+sjWzHlyUdw+NQbudnD0lSVuJAbf2Mou4QEesCAbd47qcWZMXhsvbhtxKhtLDhADGMuuuXT5VI54CmOlG5287/1XpgE4fbkw0LX8VB+VqYrFh2RtUTXUgK4F9PRYbiQDqCCRca7x7mmRaJMUyJumBl6BkDSArm2vTfxH1qBYAr6I8T8lpAX/AOznYsUY/aWLF40bLhowLviJwdMi+tYiw79fVrl46vKT6invxfJE4ridNg6LtODicU7pjH1Ro3I+6rvSNLGzAXu1wQxvwtXHeJUOxTV4ePteL+nInYmujePaaBWkt1il4pLaDrY3MbkDkStx3Gs9emoTstt15PUkiVFVgV/anQ+Kedp2mxCBwoeOOUpG5UZQzAC97ADfwrXTxcoQypLzauxWB8NgcDg5imEwTyYhVBYxi7Kr8HmlcAXte178bVOUqtWF6k7Lx+yESX7UHZ6+KTDs7ZFEmVgx0t24yyi5awBIJIIFZZUd8rvbl+SVxyaOsrQwORKAAMdgY5VKSoHXkeHeDvB7xVlKtOlLNB2YNJlG230MeO7wXkT2f3i+Htj4+NegwnSsKnZq6Pnw/BVKnbYrBSuuVmrUwEkUAJtQBugBS0AOAUAOLQAsKKAF5BQMQ+CjbeinxUUAMNseE/uwPC4+VFwNfsdPVaRfCRvrRcDTYB1GmIkFvayt8xRcC+9ANgOsXXzMWd/9MFQpWPgxA9Zt/hbdc0M3YeGTtPcskkNqRtUrgGKwt+FItjK5QelWzep7WRjG2hyjNkPeN9v85VJM5eKw+R5o7fIo0un+4I+YqZiEJYnePOgRK9H5SJ0HMsPNG/2pgy4g1IrN3oA3egCCoGVrbB7b/q/vUCwl+gfRZ9oYhYhdYk7cz+ymmg/M1iB7zwrHjMUsPTvxew4q56JOx4MiRiNQsSlYsos0QKlCY2GqnKSLjWvK9bO7d99/HzLrEWuIxeF7DwyYuMaJLEU6+3BZkYqGP51OvECrstKrqmovk9vc/oGoPhZJ8Ls6ed0CzE4jEZCbhGkkZkViNDbMt/fU5KFWvGCemi9A4B2y8JjIXj6zENiUe4kzJGhibLmDIUtdbjLlIJ7QN9KrqTpSTtHLbbfUNSfU1nGRuL2XJ1hmw83VOwAcMnWRSZdFJW4IYDS4I033sK0RqLLlmrr0YgDaccwQtjcTAmHWzOIo2UvlIIUs7tYEgaKLncDU4uDdqcW5eLAFh2pjpAZFwIEZN06yYRzMltCY8pAJ1NiRUJ0KMdHU18FdeoXCMBjVmVmCsjIxSRHADxuACVNiQdCCCCQQRWarSdN24PVPmNGSLVJIbFDGRO2+jkOIu1skntqN/wCoet8++t2E6Rq4fTePL7EJQTOfbY2TLh2yyAa3ysDdWA328xoa9NhsVTxEc0H5+BS4tEca0kRBoAygDYoAcU0ALBoAcU0DHFNAC6QGKKAN0ASHRfZP3yY5heCIjrOUj71i7xuLe4caZfRp5nd7HUFccxpwHCg2CnQGgE7AcsVItUgPEYJXBVgCDoRzFFibldWZzzpFsJsO17XjPoty/K3f86Zy61Fwd1sV/FQKVN1G48KZQRmy3tLCfzR/EhT86kRLuKsKzd6QG70AQlAyAkwUk+IEMSlpJJMqgczz5AbyeABqipUjCLlLZFiR6M6G9Go8BhlgTtN6Uj29OQ7z4DcByHjXkcViZV6jk/d4IvSsidFZxm7UAVHbvR/ELBNDg8rxTI6GGRiOqLgjNC+tl1v1Z05Ebq3Ua8HOMqm64rj5/ci0WuKwCoSM2XnqbWBNvLzrG1fUkUfZsmMOMkkiwwS03V4pPvF43GVSsqxsAVfIUII3jQjl0ZqkqSUpX0vHT4X8yJc8PtGJ5JIVcGSO2dNzAEAg2O8a7xpWF05KKk1oxjmKwccmXrEV8jB1zAHK4BAYX4gE699JScb2YxnaeNihQyTSLGg9ZjYeA5nuFKFOU3aKuwKBs/pJAZAIC0WHVmchIZZ5sSxuGaQhW6tL21JLGw9Hcd9XCTy9rWW26SXltd/DzIplhwe1YJywhkDMtsy6q633ZkYAjyrnVKE6feRJMWwqkkaLWFzoKVruyGcu6R7SOImZ/VHZQflHH36n317HA4b/AB6Sjx3fmZpSuyKyVsIiStACTQBsCgBQoAUtIBwUxjqGgBykBu9MBgRyTyphof8AUk3neI09Z27gPM2oJwg5OyOky7Miw2EWJCwSMqdCwaQ37WbJqS1z7yOVBucVGNhzD46GCLOYnhVmIAK3dtL5yNTuB362FAZklexMQzBgGU3BAIPMHdQS3ApZFkkUqxBXODvFiGS4ZTzBPwIpAtxRbUjiADu4G4Gu7gaC0F2nCHQggEcQd1DJwSejOb7W2SVuUFxy4jw5ihMx4jBOPahtyKXGbZD7Jv8Ayuf7VYc8vrHWplRq9AG70ARAoGdN+zHob92DYyZfx5fQBGsUR+TNoTyFhzry/SeM62XVx2XxZphG2pfbVyiZgoAVTAymADtXZEc+UkskiX6uWM5ZIybXytxBsLqQQbairKdVw8nunsxENDCcPNIuJxRLYsBElWMRKrIpVQXuV64h7jQXybtLVe2qkU4R7u6vf9QgLo5sVnmMuIxU8k2DleM3KZGUoGU6JmysjqSubeDVtaqlHLCKSkr/ALrbcEg3o90obEYl4xGxhYF4ZuqkQZRYFHzixN7kMDbhaq62GVOCd9eKugTLBi8DFLl6yNHynMudQ2VrEXFxobE699ZoylHuuwyIxUAjx0UhHZlhaBTwV1brQoH5lDH/AKdWK8qLXJ3+n75hxDpsML3sL2te2tuV+VZXe1hgc2HqsZTunG0+rTqFPakHa7k/33eANdfonC559bLZbef4ITlpYoVelKRJoAQ1ACDQBtaAF0AbFIBa0xji0AOCkALtDGiNb7ydABvJ4CmB0ToF0bOGhMsw/wDcTWaT8i71jHK3Hv8AAUG+lDKvEs1BcQUmyQ2IBkQyKWd8zksgW1hHkY2Ugm4sNQKCvJd6kl95YTCMquVlJQg9rs5cwZbab9CKCd9bG8VhbnrEsstsoY3IsSL3UekQL2v9TQFuRC4gN6EEjL1ZbrJ5DdCx9IEHRzfwC/CgWuyfvJDCD8JbnMbanNnueJz8aTLqb0RAbSg1NRNcWU/b2wBIC0dlfXTcrE8+R76anYyYjBKp2oaP5hmul9DYX8q0J6HCnFxk00ZemRMvQANsrFLFMkjRiQKwbI2ga26/z91U1oOcHFO1+JJOzOx9GOmOEx2kT2lHpRPYSDmQPWXvF/dXkcTg6lB9pac+BqUkyeNZRmUwN0AbFMDdADWKwqSoY5EV0YWZWAKkd4NSjJxd09REJ+ynwljgYkKEs0sJYh5CQoDJK5NiAtspsDfeKv6xVf7Xrwf4FsNdGcWYocS0sckEEcryIJlysqMokdRYkFQ5e1idCAKnXhmlFRaba4enyBCcFj9o4orLFHDh4CQV64M80qXGuVSBGCL/AApyp0aekm2/DZfcLsl8Jj8PiWdUIk6h1BOW6rIBcZW3EjXduqmVOdNJvS6+AB5SqWhkftfERwRPNJoqC/eeAA7ybD306VGVSahHdg3Y4t97afFLI/pPKl+QGYAKO4Cw91exwlGNPLCOysZMQ/45PwfyL/Ps9G9JFPioPzFd1xi90eZjOa2bXvI+bo9Ad8SjwuvyNVuhTfsl0cXXj7QDN0ShO7Ovg1/mDUHhKb2uXR6RrLezAJuh3syn3rf5EVU8EuEi+PSj9qHxA5eik43FG95B+VVvBz4NF0ekqT3TQK+wcSP3RPgQfgDeq3hqi4F8cbQl7QJLhJF9KN18VI+Yqpwkt0XxqwltJeo2DUSYoNQM1PiAoJJ0FAEr9mmxfvc7Y2WxjhbLGu+8uhzEclBB8SOVBooQv2mdZYUGsQRQME2hgVmQxvex4g2II3EHnQEkmrEQbYVCRDmmY9WhUM3WaXBtclQOI5rpwoK32FtqG7Gx3WRi6yXAHbdAoc6gkWJ4jdQTg7oTtnDZ0XsZwrBmT21swIHMjNmHeKByV0J2VsyOMFoy2VgLKx0FvEXv466UDhFR2A9qR2NQZrg7ohJ4qTLkwCaH/OVOMnEpxGGhWWu/MBbQ2rSndHnJxyycbic1MiApvpAVKSZkkzozKwNwykqykcQRqDVMoqSs0WHT+hv2vulotoAuu4ToO2P1oPTHeNe41xsT0Un2qWnh9ixT5nYdm7QhnjEsEiyI25lNx4dx7jrXFnTlB5ZKzJ3CqgM3amBlMRsUAbpgQvSrZ0mIjjiQAoZ4TMpNs0KtdwOeoXTuNX4eooScnydvMTF7ftIv3NJjDLMjFWCE9hCvWAHcDlNt99b8KVLsvrGrpfqAFi2vgMERg1bIIwL2R2VM24yuBZSd9zzqx0qtX+R63/dALEKzWA5V9p23utlGFjPYiN3t60vLwUaeJPKu70bhssese728vyQk+BT9nNaeHvmhHnIors0e+vMzYj+qXkzreSuweaNdUKAENh6AGzEaBiTH3UAa6scqAsJaIUBZAk+zUbeqnxAPzpOKe6JKUo91tETjNhQ//WB4afKqnQpv2S6OLrx9o5x0yw5WQql8gtpv1tf61z60Yxm0jt4Wcp0lKW5H9FOkk2Bm6yPVTYSRk9mReR5MNbHh4XBqNlObiz0BsLbMOLhWeFrqdCPWVuKsOBH+9I2xaaug0igkJNAxNAyEnWRcmGSRY7h2MlrtbMezGp0zAEXJ3UENe6h/C7RjdjGjl8gGZ9633WL7i3cKCaknogy9IkR+04riky6myAlWkXoitpYjL2Rv49w/vU6cL6swY7FZFkju/gRWarziGXoGBikBUcTv95qssEOu7w+poYEl0f6Q4nBSdZhpSh0zLvRxydDofnytVFahTqq00NOx2voZ9quGxWWLE2w8xsLk/gufyufRPc3ma4OJ6MnT7UNV8SxSudFFc0mZTA3QIymBsCgAHa214cOFaZiM5yqFRnZmsTYBATuBq2nSlN2iIoPSHHwy4n8F8TBFKB96kEcwWRQMoURZL57aZtBbnXSowlGHaSbWyutPeJlr6UbVTZ+DAj0bKIoF36gWB11IUa693Os2GouvV182DdkcTZrm5JJOpJ1JJ33r0iViobWa0+G78RB8JFP0q2l315lVb+uXk/kdTjxEs2JniWQxJB1a6RqxdnQSE5muBa4Frd99dOknKUmk7WOE4QhTjJq7lfjydh2PbKpnSU5pEkEQCKSZWKLIuVBuOVteAIPCmqltHuDw7dnHZq+vDgGwY5CSr3jdVzsr2BVLkZiwJW2h41LOtmVulJarXhoEYd0kXNGyuvNSGHmKFJPYUoOLs1YxoqkREGCgBtoKAGXiNAAWJjNqAOcdIY/x5B3j+kVycT/Yz0GC/oj+8SqbT2X6yeVVJmsc6JdJpsBNnTVDYSRk6Ov0YcD9KZOnNxZ37Y+1YsTEs0LZkbzB4qw4EUjcpJq6C2FBITQAJtDBRzLkkUMLg27xyPCgHFNWZD49g98JCoXQiS62WOPmBuJb1feeFAm79lBOxsRnUhQxjSyJIxuZbCzN4X48aRKLugyZbihlsXYqfSHFCEbxna+RedrXPgLjzFKw61dUo34lH2TMzISxJbO9yd5JN/rV8djhVG5O7DM1SKzM1Awa9JgipYjf5/OqywxuHh9TQAkigBJSlYC4dDvtGxmBsl+ugH7pyeyP+W+9PDUd1YMTgKdbXZ8/uTUmjufRTpng8ev4ElpALtE/ZkXnp6w71uK4OIwlSi+0tOfAsTTLFWcZu1AG7UwNgUwsYTbjUkKxwzpvt/73iSyn8JLpF3i+reLHXwtXpcHQ6qnZ7vcqkyvkVrIkbjZbT4bulRvJlqdPvIhV7j8mdkw2yLy4l5M655QyFJWQlBDEgvkYcUOhrpqnq2+f0OBKtaMFHguXi3xHX2GEKPhisbp1gu4aQN1mXMxJYMX7I1J5ih07axGq97qpqnbbTb6GsDsUo2IaVjP1yIpvbOwAbOLaBfS0AOlqiqdm763Jyr5lFR0sZLMGieGUmMjLkkkBiWQg5lVjoC3Ys1t41HIRb0sycY2kpR18Frb94GS7TReokV8sN5o5AzZgrBC4udbkFCBbeDpwp50rPhqJ0m1KLWujQV+2Iuo+8C5U6AWs7NfKECn1i2lqs6xZcxQqMs+R/viOptaBiVzG6+nZWZYzxDuoKgjjrUesRJ0JWv8Ar9wiTaeHD9X1q5r5SNSFa+UBmAspvpYkU+sje1xdRO17DW2bpEzLbMSqLcXGZ2CLpx1NOcrLQVKClKz2+xznpfDkxco/SfNFrm4j+xnawb/hj+8SEYVQayJ2ls0Nquh+dSTAX0Q6TzbPmuAWjawkj9ocxyYcD7qZOnUcGd62ZtGLERLNC2ZHFwR8QRwI4ikbk01dBBoJiWoGDYiIn0SAbrc2BuoNyvvFx3XpDImfaoiZkEX4cQUMwZFyAgEWQ6lQCN3gL0EHO2ltESGKxCojOxsqgknuFBY3bVnHdq7UafGCQ6AqyqPZUagePE00cyrUc5XEbO0Mq8nv5qpqyJnkFlqmQNZqAMgw7yXVBc2Jtp9aVrl9DD1K0stNXZG/8IYtvUVd/pOvP8pNLJI6Ueh8U94pebX0uEr0JnNrvGNAN7H6UZGXx6CrveSXr9hxehRHpTD3J9S1LKaI9AP2qnw/IQnRKIb2dveB8hUbGqHQNBd6TfovoL/4cgHqX8WY/C9qrdzTDojCR9j1b+5keCETBo1CMDcMoswPMEag1nqRbVmaI4SjDuwXoi+dHPtEkjtHiwZF3dYtusH6hufx0PjXJr4FPWHoc3FdERl2qOj5cPwdH2dj4p0EkLq6niOB5Ebwe41zZQcXaSOBVozpSyzVmFikVm6YFT+0Ta3V4doEPblVr23qljfz3eF66fR2HzzzvZfM3YXButTqTeyTt52OLA13jkG70wK7tye0yH2bH43+lSjoKSurHobF4d2IyTNHbeFWNgfHOpPlXYkm9nY8zCUVvG/qNDDYkbsRGf1wXPmki/Ko2lz+BNSpvePx/DHAcUPVgf8AieP6NS7XgP8Ai8V6P7DoxUo0fDMeeR0ceTFSfKld8USUY8Jet19wbEvhWULKmRVYPZ42jUONxzWCnzqLyPcnFVU7xd+G9xuHZsbTdcsudQxkVAQUWVgFZ7jebcOBJPGmopu9yMqklHK1Z7X8OQmLY8gXqOtAg1uoS0jKTcqz5rWNzcgAml1bta+hLr43zW7Xnp6CThXw2GYIAztIXZshcDO98+QatlW2g5UsrjHQlnVSor7W/UCxuGaFQ80l5lLPKrIDkSR+whAAAKruHLU1G92lruSs0pOyWmy8bLUrP2jRWxQPtRqfeCy/QVmxS7ZuwDvSt4lVNZTcJYUAAY7AhxyPA00wF9Euk02zZtQWhc/iR8/zpycfHceYluWU6jg/A7ps/HxzxLNE4dHF1YfEEcCDoQd1I3Jpq6HmoJIGxWfKchUNwzAlfeAb0h68CBxOzZpJo5JoYZAunZYjeR2irL2ra2W9taZW4tyTaRXen+2szfdkOi6yHm3Bfdv8fCkU4mp7KKKWtNGe8jzBqRjDYX/FkHch+Y+lSiRmEF6mViM9AyU6PSWnXvzD4E/SpR3Op0PPLio+N18PwW0irT2YgrUbDGpEqLQ0DvHUGiVxpo6g0MYkhquUQBZMNVMqY7C9nYybDvnhco3duI5MNzDxrLVoKatJFVahCtHLNXR0jo70+jksmJAjfdnF+rbx4p8R31zKuBlHWGq+J5/F9DTh2qOq5cfz+6FwmxKKhkJGQDNcai3dzrJCnKclBLVnHhSlKaglrscq2vimnlaRt7cOS7gPcK9dQoKlBQR7ShQjSpKmv3mUUrYkcjbyoPBTjlk0+Bs0yBUtsPeVvcKktgPRePgaSMMjyqwUsOrYKWOXRTmBBv3iuvJXWh5mnJRlZpe8jtmbQxC4OSeZo5CqMygaMCoN0lsAMwIANgONVRnJQcmaKlKm6qhFNfvAK2XtWVpupkRWOUMzxBwqEjMquGFgSN1ifCnGbcsrFUowUM8X7nx8iVG0Iu2S4AjYK5OgViFIFz3MvnUsy1KlTlppvsPyYhVKgsAWNlB4mxNh7gad0hKLd2uAxiNnQubvEhPMqM3uO+k4p8CSqTjsxr9mKPQeVPCRiP5XuvwpZOQ+sb3Sfu+xnUTr6Myt/wDpGLn+JCoH8tFpcx5oPePo/uKjaXMBJEv6lfMBodbMARy0vvou+KBqNtGUz7UYrNA/MSL5FSPmayYtbM6HRz0kvIooNYjpmGgBJoGWbo90OTE4Z5JluHNo7aFQuhYHxuP4a5eMxkqdRKD23K5yswHZ0eK2PKSM02Dc/iAeknDPl4MBxGhA1tpbVh8bCro9GXUa+V6nUMHjI5o1liYOji6sNxH0PdWs6Kd1dCiKCRDdKNsDDQF/XbsoPzc/Ab/LnQV1J5I3OQyuSSSbkm5J3kneTTOc9QSdrPGeTj46UyLHcLJ+IxPFR8Cf704BUQYXqwqG89AyS2fLlkRuTDyvrQacFPJXhLxReavPemiKAAcLi8zSq1h1b5L8wVVgT39r4VWnqyqlWzSmnwdvgn9R9loaLxmQcd1RaHe24wJEIuGUgmwIIIJ5A86gJVItXTQHi8bGpsO298oRdWLWva3DQg3NQaRTUxdOGi1ltZb3EwTZg+ZCrR+ktwdCuYWI01qLgOliXJSzRs47rfhcHWR5iEw5sLAvIRcJmFwoHFrH3VFU7lMsVOv2KDsrXcuV+CXP5FnwksiQiEyMy6ZgdzMONtw110qxUIKWe2vMujRjdTlrJK1+IhquLSp7RjtK47yfPX61TLc8P0hDJiZrxv66gjtpUTGU7Ftd2PfUxHpWBZHgiMbhCUQ3KZwQUGhFxz5119WlZnmezGTzK5H47Y+IdZ/xIy0sRTKqFA7cGYl27VrrfvF9wqqUJNPXdGinWppx0ejvvf6GY/GBLSLFNHMoAy9UzCVR+7Zo8ynjY30J5XBUpW1SdyVOGbstprz28ddQeTZTzT4hwbhJInWFhZJH6qMnOfDQcAb99QcHKTfwLVVUIRXNNX5asmJT1/USR/u5bsDoy9h0dSPaBYC1WvtWa5mdfx5oy4r7Mj8RiZYppcTPG+WON1j6uxjKaMSzXvnOUDUACoNtScpItUYzgoQe71vuE42OVphmnkiicKI+rCDt21V2Kk5jw4bxv3uSbe9kQg4qGkU2t7/QkmmSBF62XQaZ5GUFj32sCfAVO6itWVZZTl2Y+hrF40qEMcbS5z6hWwGUte5Ntbaa0OVrWVxwgnfM7WKr9orrLhIpk1AkHiAVYG/I3UCs2J7UE0bcCnCq4vkc3vWA6xmagAjZuDaaVIU9J2CjuvvJ7gLn3VCpNQi5PgDdju2EwSRxpEgsqKFHgBbzrzM5OUm3xKXqBbQ2YHB0qGwinR4R8BIXiUmFzeSIbgfbjHBuY3H411MLjmuzM04evldnsWiHEo6CRWBQi4bhbj4V2FJNXR0001c5J0r2ycTOWB/DXsxj8vE+JOvlypmCrPPLwIImmVAuNOgPIj5imRFQn8QeB+YogOoFs9WlQ3npDDp2srW9k/Km9gi7O6OgYabOiv7Sq3mL1endH0OEs0VLmrjtBIgItnxPPiDKitlZCM2qhTGutjpwOtU5U5O5z4UKU61R1EnZrfyQjFtBD2sO6h7j8JGuJBfUdWNx5EUpZV3QqSpUdaLV/wDVPf3fUcmjWSaTriOriCFUY2Q3BJdhx1FtdNKGrvUnJRqVZda+zG1k9teL5gbjrZoAkeWAMzA5bB2Vb5rct1r79aju1yKJN1a1PLG0E29t2lv5cuYXsrC3lnmK2JcotxrlQAG3cSPhTitWzRhad6tSq1q3ZeS+4VHgXDTtoTIAEHIKlhm95NSy6stVKSdSX+23uQ1gtjGOGNUbLInavvVmI7QYcV4e4UlT08SmlhHTpRjF2ktfBvjfwJKB2KguuVuIvcA9x4ipLxNkHJxvJWZj0EyubeS0gPtL8R/gqme55TpunlrqXNfIhMYSFNQOMVJzqasInpjo5JmwmGbnDEf/ABrXWh3UearK1SXmyTFMgbpDNg0DuNTYZGDKyizEFraXItY3Gt9Br3Ck0mSU2ncTjsIsqNG98rWvY23EH6UpRurMcJuEsyGcbswSZrOy5tGAsUbSwujXAOg1FjoNaUoXJwquNtBjE7PkHVyBlkkiRlvICA1wLvp6L9nf3moOL0fFFkakdY2sm+H7sRmzpZGwcKYYhtAsxUjrEuMzBM1lzanW+nyri24JR95fNRVZufu5e8T0phU7OlRInjEQjIVxY2DLcggkNpe5vRVS6ppLYKDarpt3vyOUXrnHYMzUAX37G9n9ZiZsQR2YVCKf+ZJqbd4Rf/JWDHS7KjzIyZ0PpHPIoEWGAOIkByX9GNR6Uj9wvpzNq50KUb5pbL9sRSI+Pbqxu8WLkhjkTJ6LnKQwvuYAgjjw1FRlQbSlBNoViQxWDVxuGtZrCsReG6MxqksZLZJbgqCQBfQkW3E1pp4qrBWTLVWmo5Uzm/SjoLNh7vDeaLuH4ijvUekO8eQrp4fHwnpPR/ASmnuUxjXQJA2MPZNNCNK3aU+I+FNDkEs1WFY0WoAlMQew3gflQ9gjuW/olPnwkJ5Lk/kJX6VbTd4nuejp58LB+FvTQmKmbBowLcnKLsAG09IC9geY1PnSsiOSN27b7mRQKvoqq+AA+VFrBGEY7KwibBRuQzxqxG4soJHgTScU9xTpU5tOUU2vAXNIqKWYhVG8nQCh2RKU4xV5PQXlosSuM4rFrHkzXAdsoNuyCd2Y8L7qTaW5VUqxg1m4u3/RMuNVZUisSzgnTcoHFuQ4UOVnYUq0VUVPi/3UDxO2EDlESSRlNmEa3AO/VjpUHPXQqljIqThFOTW9l9dhc2OAlSLKSXVmJ9kC28d50ob1sWyrpVY07atN+ViO2+uityJHmP8Aaq5nJ6dp3pwnydvX/hW9pyWjPhUEeYKnUyJ6R6FvfAYU/wDIiHkoH0rqUu4vI85iP7ZebJurCo3SGbFIDdAzVAGUDBsbs9JSvWZiov2MxCMfzKPS9+lQlFS3LIVJQ2C40AACgADQACwHgBTtYTberA9vYfrMNOntRSAeOU2+NQqK8WiylLLUi/E4LmrknoQfF4jKpNCQM7b9myR4LZsAkDGXE5sQURGeRs9stlAvogSuViL1Kja2WhDcva2NmtvHEWIB1seI8KytCIjE4FYIpWhi6yRszG5BZ2Y73Y6lRfdyFhT78kpPQCM2biZI4Ih92mMaxoA4MbEqFHaKB827WwuahUpJybzK/vBomSKzERjER3FJoTRQ+lPRKGa7gdXJ7SjefzLubx399asPjalLTdchKbRy7b+xZsPcSL2dwddVPv4HuNdyhiadZdl68uJapKWxGFtEPh8iK0Lcm9h1mqZWIvQBL4o9hvCm9gW5OdBMYBhZM26NmOmpylQ27+ap03ZM9Z0PWSwsr+y36bllwmMSRBIjXU313bt9xwNWKSaujq06sKkM8XdAmBmmmw6OGVHbW+XMALm2hO+1qhFuUblNKdWrQUk0m/C4jZsssuFPbtKesUNYCzBiFNrdwoi3KPiQoSqVcPv2tVf3gO0tmD8FM8jSyMoJaVmyqozSEDQd27jUJQ2XFmevh12I5m5N83stWP8ASRnZoYQv4byJma411vltv3KT5VKpfRFmNzylCml2W1d/QlNpYrqonk3lVJA5ncB52qcnZXNdep1dOU+SGsHG8kAXEqMzAhxpuubbtxtY0ldx7RCnGVSlastXuAdG4iOtd2LOHaLMx1CR2sPrUKa3uUYGDWeU3d3tfwQ1hsXHC4SORJUkckBSGkRmNyTl9JO86jvqKaT0YqVWFGahCSkpPhq035brx4AkmKjTGO4LykoVIRS5Rgw7IAGgsCaTazXK+thDFykm5aW0V7O+wfthbxN3WNEti/pWnnwsvDX0KZtcnJVaPFsr3VmpiLnsX7SMZhokhWOFkjAUZkfNbxVxV8MRKKsYqmBpzk5Nu7JuH7YJPXwiH9MhX5qas/y/AofRq4S+BIwfbBB6+FlH6WVvnapLFR5Fb6NnwkiQw32sYBvSWdO9o1I/7XJ+FSWJgQfR9VbWJLD/AGjbMbT7zl/VHIPjltUlXhzIPB1l7PyJGHpds9t2Mw/vkVf6iKl1sOZD/Hqr2X6EjBtGF/Qmja/syK3yNSuivLJcAtTfdQAoUhmEcKBnnfHR9XI6ewzJ/KxH0rkNWdj0cXdJgGBwjYvFQ4Zb/iSJHpwDMAx9wufdUZyyRcgZ6f2hsjMF6oqhVRGMykgKCCtspBVlIBBBriRnbcSBgHkmMbyyxyCMEBDZboxBfKRlZWDqbdxG8VLRRvYA2PHBXWGTOX0HWdWyxM1rgBt1yBuvUHC6uhWA9obHcI33aWSNjchAy9VmPcytkHGy2oUlftK4A+BgEDLh16yaRvxJpGJ0BBAYk8yuUKOA7qrqRzrNsuCEzW0sSuHGVFLySMxSMHVmJuxufRQXuTuHwqqMHLV7LiIBXByKh6587sSxsLKt7dlBvyjv1NVVHFvsqyIyIPH4cG4YAg6EEXBHIg7xUYtp3W5U1xKTtzoWrdvDHKd/Vk9k6+q3q+B08K6uG6Sa7NX1+5ZGtwkUuUEEg7wSD4jQ7q7id1dFo1emMmMYew3h9abEtwv7P5LnERH1kU28Lqf6hTp72PQ9CO/WU+a+6+pKbIcwwJMLmKRLSAa5HF1EgHI2sfcaUOzG5rw16NGNRd1rXwe1/v6ktsnFJHhYWdgoyqLnny8asg0oK5tw1SNPDQcnbRG+jjXje24Sy5dCLqWzAi/DWinx8wwT7Ev/AE/ncfOFc4kSmxQRFV11DFrtp3jjTs89yzqpdfne1rLzuM7RwWIlkWzxoiNmQhSz3sRqDpxNKUZNlVajWqTTUkkndaXf2GukkLmFQZDYFFeygZ7sovf1bb9KVRPLuQx0JOku1yv46r0JTC4ZY1yrmt+Zixv4mppWNtOmqccq+dxrDYQIZCCT1jlyDbQkAG3lSSsKnSUHJri7ihGo3KB4AClYsUYrZDbVFkrA2IS4I5gioshWhnpyhzTRVJIbiqDwDB/uS8qLiGjgV5CncBs7PXlRcVhp9nLTuFhh9nCncVhh8FTuFhs4Wi4WEnCmi4DuHMieg7r+liPkaeZoi4J7oncDtzFpuxU4/wCtIR5FrUdZPmxOhTe8V6EtD032gu7Esf1KjfNb1JV6i4lbwlF+yVra+PZ2eRrZ3ZmawsCzG5Nhu1NVt3dy5JRSSLb9hey+t2iZiLiCN3v+d/w1+DOfdWPGytTtzA9D1ygNOtwRe2lrjeO8UwITA7GdZQ0zGe1ykjOwKHh+F6O4ntDyqyU01ZaDDMJtNJGyhXXVgrMoCvlNmyG+trHQ2NhUZQaQmgp15VU0RIvZuzSt5Ze1PIBnbgo4RpyQfE60VNdFsArF4fSs0oiZW9pYWq0VtHP+nm2uoj6pDaSQHUHVE3E9xO4e/lXRwGG6yeeWy+LHCF3c51evQlwm9MCd2hERExPd/UKr62MnlRb1MoxzMY6ET5cYo9tWT/tzD4qKshudHoeeXFJc019fodD2bghFEIr5lGbeBqCSbEe+r4xsrHqaNBUqap7oJggVFCqAFG4DcKaSWxZGEYLLFWQ5TJG6ANgUCGsTh1dSji6neLkd+8bqTSasyFSEZxyy2HKCYk0mA0wpDGmFRaGIK0rAVjGRlZGFuJ8jr9azyVmeGxtPq8ROPj89Rm1IyiQlACMlACHWmAw4oEDOKYDeWgDWWgDAKAFXpAIkksKAIyeS5qRE7p/6etnZcLiMQRrJKIweaxrfT3yN5VzMbK8kgOrWrEBu1MBErEAkKWIBIAtc9wvpRYCBweDb7y87YUp2exZo/Ssc5YBvSbdfzq1vs5bjHsJtvrDI2ULFGpYljaQ23kKNCujC994qMqdrLiJoRsjbXXInYdmNg7Ih6tWO8Zjy0va9KdLKJolXjqhxFYA2hhFysx0ABJPIAXNVOlfYTR5Z25tNsTNJM1+2TYeyvqr7hb416WhSVKCgiaVkTeztkRPEjENcqCddL8a6tLDwlBNnLrYupCo4oI/YMPJv5jVn+LTKv86r+oY2z/ot7vmK8/Q756mv3CvbInyYiJ+TpfwuAfgTW1FWDqZK8JeKOxLWpHu2KtQIy1AG6AN0CNUAZQBlqQCGFIBplpDE5aVgIDb0dpAeY+I0/tVFRWZ5XpqnlrqXNfL9RHXqs45hNACGoAZkNMAeQ0ADvTAbNAhBNAGi1AGi1AAmJlpiBL0CPUn2UYHqtlYVfbQynxkZn+AIHurjYiV6jAttUgZTAygDRWgAX9nx9V1BW8eUJa/qjTePCnmd7gIji6p3IAEZUObblZAFOnIqF3eyaHqBF4BwZQ0Kz9W2d5GlzCMggsuQPre9t1hapyWlna4MC6Y7WU7KxcyZl/AcDMpVgZFyrv3+mNRpRTp/yJPmK2p5gP8Anwrtki7dHRfDxnxHkxrrYbWmjg43StL94En1daLGTMVzbB/CN+7515aj3j29fuFXatZiOz7PmDxJJ7Sq3moNao7Hv6U88Iy5pMIvTLRQpiNigRugRo0hmWoAy1AjRFAxBWogYVosFyC6SOhVbMpYEiwIJsRr8hVNW3A4HTUqcoxtJXT58CBBqg86YTQAhmoAZc0wGHNADDmmIaJoAQTTASTSAQ5pgCyLQIatQBYeinTTGbPa+Hl/Dvdon7UTfw+qe9bGqatGFTda8xHcOh/2rYLGZY5T92mOmWQ/hsfyS7vcbHxrn1MNOGu6Av8AWcDKAMoAymBlAEXjdnMI3EBIzKy5L9jtaErf0Da+g0+dTjLVXGVX7XJv/hpQFZLtAmVhYi0yaaaH0d40NW4dfyoR5vffXWGT+xYJ2ivG4CgkWObfvO7xqyMpJaMhKnBu7SC/umL9tfNv71LNLmLq4ckZt8jqjqN40rmYfvHTxPcKk2+tpgOq9DJ8+DjvvXMn8rG3wtWin3T2nRdTPhY+GnoTdqsOgKFAhVAjKAMtQFwTE7Tgj/1Jo17iwv5b6i5RXEoqYmlT78kveReI6YYVfRLv+lCPi1qg6sTFPpfDR2bfkvvYjpumhP8Apwgd7Nf/ALQPrUHWfBGOp05/pD1f78wKXpFiH9cKOSqB8Tc/Gq3Uk+JiqdLYmWzt5L73A5MQ7emzN+pifnUG2zFUr1Knfk37zA450ikV168x5igBLYlfaHmKAG2xSe2vmKYDL4pPaHmKLAIecU7AMtKP8BoENlqYCS3ePeyj5mgQk+K/zp/egDRH5l/nU/I0AMMw5jzv8qAGmIoAReiwGXoEXDoh9o+OwFkV+thGnUy3KgfkbengNO6s9XDwnrswO2dEvtNwONsmfqJj+6lIFzyST0X8ND3VgqYecN9gLrVAGUwMoA3QBR/tkxHV7MkbIj2ki7LglfTG8AitOF/sQHm3HYvrGzZI00taNco8bc66ox/AGYLeMsADrYka+FWQhKSuiudWMHZhX7XxQ0zP/nuoyzDrI8z/2Q==")
        if "ok" not in st.session_state:
            st.session_state.ok = False
        
        if "ErRoR" not in st.session_state:
            st.session_state.ErRoR = None
        
        if "ErRoR2" not in st.session_state:
            st.session_state.ErRoR2 = None
        
        
        st.text_input("Password", key="password")
         
        if st.button("Enter"):
            if st.session_state.password == "3BK!45g2":
                st.session_state.ok = True
            else:
                st.error("Wrong password")
        
        
        # ---- GIỮ LOGIC CŨ ----
        if st.session_state.ok:
            st.title("Welcome!")
        
            st.session_state.ErRoR = st.selectbox(
                "Your choice:",
                ["rock", "paper", "scissors"]
            )
        
            if st.button("Sure"):
                st.session_state.ErRoR2 = random.choice(
                    ["rock", "paper", "scissors"]
                )
        
        
        if st.session_state.ErRoR2:
            if st.session_state.ErRoR == st.session_state.ErRoR2:
                st.image("https://i.ytimg.com/vi/9xhVwqK4G-A/maxresdefault.jpg")
                st.success("Draw!")
            else:
                st.error(st.session_state.ErRoR2)
    with tabD:
        st.title("Maths Game!")
        steps=0
        operation="let's see"
        a=random.randint(-1000,1000)
        b=random.randint(-1000,1000)
        types_operation=random.randint(1,4)
        if steps==0:
            if types_operation==1:
                operation=(f"What's {a} + {b} ?")
            elif types_operation==2:
                operation=(f"What's {a} - {b} ?")
            elif types_operation==3:
                operation=(f"What's {a} x {b} ?")
            elif types_operation==3:
                operation=(f"What's {a} : {b} ?")
            if types_operation==1:
                result=a+b
            if types_operation==2:
                result=a-b
            if types_operation==3:
                result=a*b
            if types_operation==4:
                result=a/b
            steps+=1
        if steps==1:
            time.sleep(2)
            st.title(operation)    
            answer=st.number_input("The correct answer is:",max_value=1000000,min_value=-1000000,value=0)
            if st.button("Sure?",key="100boy"):
                st.spinner("Please wait for a moment...")
                time.sleep(2)
                a=a
                b=b
                a=a
                b=b
                a=a
                b=b
                a=a
                b=b
                steps=1
                if result==answer:
                    st.success("Correct!")
                    if st.button("Another operation?"):
                        steps=0
                else:
                    st.error("Oh no.... Your anwser is incorrect.")
                    if st.button("Another operation?"):
                        steps=0
    with tabE:
        st.title("Lucky Draw Game")

        # Initialize data
        if "new_prizes" not in st.session_state:
            st.session_state.new_prizes = []
        if "weights" not in st.session_state:
            st.session_state.weights = []

        # Add prize section
        st.subheader("➕ Add New Prize")
        col1, col2 = st.columns(2)
        with col1:
            new_prize = st.text_input("Prize Name")
        with col2:
            weight = st.number_input("Winning Probability (%)", 1, 100, 1)

        if st.button("Add"):
            if new_prize:
                st.session_state.new_prizes.append(new_prize)
                st.session_state.weights.append(weight)
                st.success(f"Added: {new_prize}")
            else:
                st.error("Please enter a prize name!")

        # Prize list section
        st.subheader("Prize List")
        if st.session_state.new_prizes:
            for i, prize in enumerate(st.session_state.new_prizes):
                st.write(
                    f"{i + 1}. {prize} | probability {st.session_state.weights[i]}%"
                )
        else:
            st.info("No prizes added yet")

        # Spin section
        st.subheader("Spin the Wheel")
        if st.button("Spin Now"):
            if st.session_state.new_prizes:
                spin_placeholder = st.empty()

                for i in range(15):
                    spin_placeholder.markdown(
                        f'## Spinning... {random.choice(st.session_state.new_prizes)}'
                    )
                    time.sleep(0.1)
                
                # Select result based on weights
                result = random.choices(
                    st.session_state.new_prizes,
                    weights = st.session_state.weights,
                    k = 1
                )[0] # Lấy phần tử đầu tiên trong list kết quả
                
                spin_placeholder.empty()
                st.balloons()
                st.success(f"Congratulations! You won: **{result}**")
            else:
                st.warning("Please add prizes first!")
        if st.button("Reset game"):
            st.session_state.new_prizes = []
            st.session_state.weights = []
            st.success("Reset successful")
    with tabbleo:
        st.title("Lucky Draw Game")
        # Initialize data
        if "new_prizes" not in st.session_state:
            st.session_state.new_prizes = []
        if "weights" not in st.session_state:
            st.session_state.weights = []
        # Add prize section
        st.subheader("➕ Add New Prize")
        col1, col2 = st.columns(2)
        with col1:
            new_prize = st.text_input("Prize Name",key="dghasfdgasdfgarsgasertgasdgsr")
        with col2:
            weight = st.number_input("Winning Probability (%)", 1, 100, 1,key="dghasfdgadfgarsgasertgasdgsr")

        if st.button("Add",key="dghasfdgadrsgasertgasdgsr"):
            if new_prize:
                st.session_state.new_prizes.append(new_prize)
                st.session_state.weights.append(weight)
                st.success(f"Added: {new_prize}")
            else:
                st.error("Please enter a prize name!")
        if st.button("Spin Now",key="dghasfdgadrsgasergsr"):
            if st.session_state.new_prizes:
                spin_placeholder = st.empty()

                for i in range(15):
                    spin_placeholder.markdown(
                        f'## Spinning ... {random.choice(st.session_state.new_prizes)}'
                    )
                    time.sleep(0.1)
                
                # Select result based on weights
                result = random.choices(
                    st.session_state.new_prizes,
                    weights = st.session_state.weights,
                    k = 1
                )[0]
                
                spin_placeholder.empty()
                st.balloons()
                st.success(f"You got {result}")
            else:
                st.error("CONGRADULATON, you got nothing because you aren't add anithing yet")
        if st.button("RESET..?"):
            st.session_state.new_prizes=[]
            st.session_state.weights=[]
            st.info("Reseted!")



                

                
        # 1	~75 cm
        # 2	~85 cm
        # 3	~95 cm
        # 4	~100 cm
        # 5 – 7	110 – 130
        # 8 – 10	130 – 140
        # 11 – 13	140 – 150
        # 14 – 16	150 – 170
        # Trên 16	160 – 18050                       