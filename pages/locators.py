class Locator(object):
    #signin page locator
    _signin_button = "ui_sign_in"
    _toggle_button = "ui_toggle_button"
    _enter_phonenumber = "ui_input_text"
    _next_button = "ui_next_button"
    _enter_otp = "ui_input_text"
    # Locator for email signin
    _enter_email = "ui_input_text"
    _successlogin = "ui_tab_Timeline"
    _failurelogin = "//XCUIElementTypeStaticText[@name='Please enter a valid email address.']"
    _coaches_corner_tab = "ui_tab_Coach's Corner"

    #Menu tab locator
    _menu_tab = "ui_tab_Menu"
    _profile_detail = "My Profile Details"
    _edit_button = "Edit"
    _save_button = "Save"
    _back_button = "Back"
    _organization = "Organizations"
    _create_org = "ui_addButton"
    _enter_orgname = "//XCUIElementTypeTextView[@value='Enter Name']"
    _profile_privacy = "Profile Privacy Settings"
    _privacy_level1 = "Only allow friends to find me and view my profile"
    _privacy_level2 = "Anyone can find me, but only friends can view my profile."
    _privacy_level3 = "Allow anyone to find me and view my profile, but only friends can interact."
    _allow_friendreq = "//XCUIElementTypeSwitch[@name='Allow friend requests']"
    _my_Training_Act = "My Training Account"
    _ok_dialog = "OK"
    _signout = "Sign Out"
    _tips1 = "Tips"
    _tips = "//XCUIElementTypeStaticText[@name='Tips']"
    _contactus = "Contact Us"
    _privacy_policy = "Privacy Policy"
    _cancel_button = "Cancel"

    # Locators for Timeline tab
    _ViewAll = "//XCUIElementTypeButton[@name='View All']"
    _like = "//XCUIElementTypeButton[@name='']"
    _close = "//XCUIElementTypeNavigationBar[@name='Likes']/XCUIElementTypeButton"


    # Locats for Create post
    _write_a_post = "ui_text_post"
    _tab_button ="ui_tag_button"
    _photo_button = "ui_photo_button"
    _photo_library = "ui_photo_library_action"
    _camera_roll = "Camera Roll"
    _moments = "Moments"
    _photo_gridview = "Photo, HDR, Landscape, March 30, 2018, 3:14 PM"
    _post_button = "ui_post_button"
    _profile_pic_button = "//XCUIElementTypeApplication[@name='Cheer District']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]"
    _recent_post = "(//XCUIElementTypeStaticText[@name='Today'])[1]"


    #Training Tab

    _switch_training_tab = "ui_tab_Training"
    _click_workout = "XCUIElementTypeCell/XCUIElementTypeStaticText"

    #Delete Friend
    _friends = "//XCUIElementTypeStaticText[@name='Friends']"
    _seeAll = "(//XCUIElementTypeButton[@name='See All'])[2]"
    #_seeAll = "XCUIElementTypeOther/XCUIElementTypeButton[2]"
    #_friends_list = "XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell"
    _friends_list = "//XCUIElementTypeApplication[@name='Cheer District']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell"
    _profile_right_bar = "ui_profile_right_bar_button"
    _unfriend_button = "ui_unfriend_Action"
    #_unfriend_button = "//*[text()[contains(.,'ui_unfriend_Action']])"

    _button_count = "//XCUIElementTypeApplication[@name='Cheer District']/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeSheet/XCUIElementTypeOther/XCUIElementTypeOther"
    _edit = "Edit"
    _menu_profile_pic ="XCUIElementTypeCell[1]"
    _skills = "//XCUIElementTypeApplication[@name='Cheer District']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeButton"

    #_skills = "XCUIElementTypeTable/XCUIElementTypeCell"
    _pending = "Pending"

    ### locators for Training tab
    _continue_training = "CONTINUE TRAINING"
    _start_button = "//XCUIElementTypeButton[@name='START']"
    _complete_button = "COMPLETE"
    _congratulations = "Congratulations"
    _number_of_exercises = "ui_exercise_stats_text"
    _number_of_weeks = "ui_section_week"
    _first_week = "//XCUIElementTypeOther[@name='ui_section_week'])[1]"
    _number_weeks = "ui_section_week"
    _Done_button = "DONE"
    _Done_Button1 = "//XCUIElementTypeButton[@name='DONE']"





