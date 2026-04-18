import json
import os
import time
import base64
import shutil

# MASTER_ACHIEVEMENTS = [
#     'F_Rogs', 'E_Rogs', 'Hidden_Shop_Trick', 'D_Rogs', 'F_NoShop', 
#     'F_Peasant', 'F_Sick', 'F_Snuff', 'F_SoulLess', 'F_Tainted', 'E_BrokenWeapon', 
#     'E_NoShop', 'E_Peasant', 'E_Sick', 'E_Sifd', 'E_SoulLess', 'E_Tainted', 'D_Cursed', 
#     'D_Hell', 'D_NoShop', 'D_Peasant', 'D_SoulLess', 'D_Tainted', 'D_TwoWeapon', 
#     'Hidden_WanderTrick', 'Reach_30Min_E', 'Surv_F_BoneGlass', 'Surv_E_ChaoticPlayground', 
#     'Surv_D_HourGlass', 'Reach_45Min_D', 'GunSlingerUnlock', 'RogueUnlock', 'ShopKeeperUnlock', 
#     'Hidden_BrokenStatuette', 'DogRogUnlock', 'ReachInfinity', 'Light_Spirit_Level_4', 
#     'MetalTransmutation_lvl4', 'Practice_Lvl30', 'Thunder_Spirit_Lvl5', 'BowLevel_5', 
#     'CleaveLevel_5', 'CrossBowLevel_1', 'DeathAuraLevel_5', 'Bow_Level_8', 'CrossbowLevel_8', 
#     'CrystalSwordLevel_8', 'DeathAuraLevel_8', 'ExplosiveVialLevel_8', 'KatanaLevel_8', 
#     'Pike_Level_8', 'SpearLevel_8', 'SwordRangLevel_8', 'ThornLevel_8', 'WindBladeLevel_8', 
#     'WormGlandLevel_8', 'FireRingLevel_1', 'FireRingLevel_5', 'FireRingLevel_7', 
#     'KunaiLevel_5', 'MagicWandLevel_5', 'PikeLevel_5', 'ShurikenLevel_5', 'SpearLevel_1', 
#     'SpearLevel_5', 'ThornLevel_1', 'ThunderStaffLevel_1', 'ThunderStaffLevel_5', 
#     'Weapon_Count_3', 'Weapon_MaxLevel', 'Weapon_MaxLevel_2', 'Weapon_MaxLevel_3', 
#     'Weapon_MaxLevel_4', 'WindBladeLevel_5', 'Attack_Speed_slow_1', 'Corruption_1', 
#     'Corruption_100', 'Corruption_20', 'Corruption_5', 'Corruption_50', 'Purification_20', 
#     'CriticalChance_1', 'CriticalChance_2', 'CriticalChance_3', 'CriticalDamage_1', 
#     'CriticalDamage_2', 'Damage_1', 'Damage_2', 'Damage_3', 'Damage_4', 'Damage_5', 
#     'Damage_6', 'Damage_Negative', 'Dash_1', 'Dash_2', 'Dash_3', 'Dash_CD_1', 'Dash_CD_2', 
#     'DefencePiercing_1', 'DefencePiercing_2', 'DefencePiercing_3', 'DefenceShredding_1', 
#     'DefenceShredding_2', 'Damage_Mitigation_1', 'Damage_Mitigation_2', 'Damage_Mitigation_3', 
#     'Damage_Mitigation_4', 'Defence_1', 'Defence_2', 'Defence_3', 'Defence_4', 
#     'Negative_Defence_1', 'Negative_Defence_2', 'Negative_Defence_3', 'FireWork', 'Health_1', 
#     'Health_2', 'Health_3', 'Health_4', 'Health_5', 'Health_Regen_1', 'Health_Regen_2', 
#     'Health_Regen_3', 'KnockBack_1', 'MoonCardDropChance_1', 'Move_Speed_1', 'Move_Speed_2', 
#     'Move_Speed_3', 'Pick_Up_Range', 'Pick_Up_Range_2', 'Piercing_35', 'PLifeTime_1', 
#     'PSize_1', 'PSize_2', 'PSpeed_1', 'PSpeed_2', 'Slow_Move_Speed_1', 'XPMultiplier_1', 
#     'XPMultiplier_Negative_1', 'Finish_C_45Min', 'Finish_D_35Min', 'Finish_E_20Min', 
#     'Finish_F_10Min', 'Reach_10Min', 'Food_1', 'Food_2', 'Food_3', 'VoidAndFood', 
#     'Kill_Boss_C1', 'Kill_Boss_C2', 'Kill_Boss_D1', 'Kill_Boss_D2', 'Kill_Boss_E1', 
#     'Kill_Elite_1', 'Kill_Elite_2', 'Kill_Elite_3', 'Kill_Elite_4', 'Kill_Golem', 
#     'Kill_Monster_100', 'Kill_Monster_100k', 'Kill_Monster_10k', 'Kill_Monster_10m', 
#     'Kill_Monster_1k', 'Kill_Monster_1m', 'death_10', 'death_2', 'death_20', 'death_30', 
#     'death_5', 'Game_Count_1', 'Game_Count_10', 'Game_Count_20', 'Game_Count_5', 
#     'Game_Count_50', '100kglobalgold', '10kglobalgold', '10kgold', '10ktotalgold', 
#     '1mglobalgold', 'KillTarget_ArcaneBeam', 'KillTarget_Bow', 'KillTarget_Cleaver', 
#     'KillTarget_Crossbow', 'KillTarget_CrystalSword', 'KillTarget_DeathAura', 
#     'KillTarget_ExplosiveVial', 'KillTarget_FIreRing', 'KillTarget_IceNova', 
#     'KillTarget_Katana', 'KillTarget_Kunai', 'KillTarget_MagicWand', 'KillTarget_MagicWisp', 
#     'KillTarget_Pike', 'KillTarget_ShamanStaff', 'KillTarget_Shuriken', 'KillTarget_Spear', 
#     'KillTarget_Swordrang', 'KillTarget_Thorn', 'KillTarget_ThrowingKnife', 
#     'KillTarget_ThunderStaff', 'KillTarget_WindBlade', 'KillTarget_WormGland', 
#     'AltarCorruption', 'BTGR_Achievement', 'GettingScammed', 'SlideShow', 'All7Sins', 
#     'EnvyAchievement', 'GluttonyAchievement', 'GreedAchievement', 'LustAchievement', 
#     'PrideAchievement', 'SlothAchievement', 'WrathAchievement', 'D_ElentorScalingHell_Corrupted', 
#     'F_True_Snuff', 'DamageTaken', 'DamageTaken_2', 'SL_100', 'SL_20', 'SL_50', 'DuelistUnlock', 
#     'SummonerUnlock', 'F_Snuff_Duelist', 'IceNova_Level8', 'AntiHero', 'BanishCard', 
#     'CommonerHero', 'ShopKeeperBestFriend', 'C_ArmorBan', 'C_FastPass', 'C_RiskOfStorm', 
#     'C_ShopKeeperVacationEnd', 'C_VildCurse', 'F_SingleArmed', 'Challenge_Completion_1', 
#     'Challenge_UnlockHardMode', 'RogNGesus', 'Ice_Spirit_Level_3', 'RuneOfNecromancy_Level_1', 
#     'BloodSyphoon_Level_1', 'StaffOfStorm_Level3', 'CriticalChance_4', 'Defence_5', 
#     'Finish_B_50Min', 'Reach_40Min_C', 'Kill_Boss_B1', 'Kill_Boss_B2', 'Kill_Boss_B3', 
#     'Kill_Boss_B4', 'Kill_Boss_B5', 'Kill_Boss_C4', 'Kill_Possesed_Candelabra', 
#     'Dried_Mushroom_Unlock', 'Giant_Worm_Summon_Weapon_Unlock', 'Goblin_Shaman_Summon_Weapon_Unlock', 
#     'Necromancer_Summon_Weapon_Unlock', 'Goblin_Hand_Unlock', 'Hard_Leather_Unlock', 
#     'Light_Crystal_Unlock', 'Long_Nail_Unlock', 'Pharaon_Mask_Unlock', 'Red_Skull_Unlock', 
#     'Weightless_Crystal_Unlock', 'Wind_Feather_Unlock', 'KillTarget_BloodSyphoon', 
#     'Golden_Idol', 'IllegalMove', 'Kill_Unkillable', 'PhaseSkipper', 'SixtyFour', 'B_Arcade', 
#     'B_DwindlingFire', 'B_MortalSoul', 'B_Overgeared', 'B_TimeParadox', 'C_LeftImpariment_Ach', 
#     'E_Plex_Hard', 'PSpeed_3', 'PSpeed_4', 'Talent_Charge_Cost_1', 'Talent_Charge_Multiplier_1', 
#     'Talent_Charge_Rate_1', 'Talent_Charge_Rate_2', 'Kill_Boss_A1', 'Kill_Boss_A2', 
#     'Kill_Boss_A3', 'Kill_Boss_A4', 'Kill_Boss_A5', 'Kill_Boss_A6', 'Kill_ProtectiveSpirit', 
#     'Bestiary_Completion_Achievement_01', 'Bestiary_Completion_Achievement_10', 
#     'Bestiary_Completion_Achievement_20', 'Bestiary_Completion_Achievement_30', 
#     'Bestiary_Completion_Achievement_50', 'Bestiary_Completion_Achievement_75', 
#     'Bestiary_Completion_Achievement_90', 'LV99MafiaBoss', 'A_BloodHanded', 'A_Pacifist', 
#     'A_Purist', 'A_Rooted', 'A_RootedCubed', 'Ach_A_Souless', 'A_Vanilla', 'Challenge_Completion_2', 
#     'Combustion_Level_30', 'Fire_Spirit_Level_1', 'Perfection_Lvl6', 'Power_7', 'DefencePiercing_4', 
#     'DefenceShredding_3', 'DefenceShredding_4', 'Defence_6', 'Defence_7', 'Health_6', 
#     'Talent_Max_Charge_1', 'Talent_Power_1', 'Talent_Power_2', 'Talent_Power_3', 'Talent_Power_4', 
#     'Kill_Boss_C3', 'Kill_Elite_5', 'Kill_Elite_6', '1Mtotalgold', '200kgold', 'EvenGodCanBleed', 
#     'BreakMirror', 'CrystalCraft', 'GoblinWorkforce', 'SomethingTerriblyWrong', 'SongOfConquest', 
#     'SongOfSouls', 'SongOfTheMighty', 'SongOfTheSlayer', 'SongOfTheWealthy', 'Card_Fire_2', 
#     'Card_Moon_1', 'Card_Moon_2', 'DamageTaken_3', 'Invested_10M', 'Invested_1M', 'AntiEquipment', 
#     'DecentEquipment', 'GettingTheGoodStuff', 'ToInfinityAndBeyond', 'Surv_C_Ribon', 
#     'Challenge_CompleteAllARankHardmodeChallenges', 'Challenge_CompleteARankChallengeExpert', 
#     'Challenge_Completion_3', 'Challenge_Completion_4', 'S_ExperienceLeak', 'S_LevelScaling', 
#     'S_TabulaRasa', 'GettingReady', 'SL_1000', 'SL_250', 'SL_500', 'SL_Cap', '10mglobalgold'
# ]

MASTER_ACHIEVEMENTS = [
    'DogRogUnlock', 'DuelistUnlock', 'GunSlingerUnlock', 'ReachInfinity', 'RogNGesus', 
    'RogueUnlock', 'ShopKeeperUnlock', 'SummonerUnlock', 'Combustion_Level_30', 
    'Fire_Spirit_Level_1', 'Ice_Spirit_Level_3', 'Light_Spirit_Level_4', 
    'MetalTransmutation_lvl4', 'Perfection_Lvl6', 'Practice_Lvl30', 
    'RuneOfNecromancy_Level_1', 'Thunder_Spirit_Lvl5', 'BloodSyphoon_Level_1', 
    'BowLevel_5', 'CleaveLevel_5', 'CrossBowLevel_1', 'DeathAuraLevel_5', 'Bow_Level_8', 
    'CrossbowLevel_8', 'CrystalSwordLevel_8', 'DeathAuraLevel_8', 'ExplosiveVialLevel_8', 
    'IceNova_Level8', 'KatanaLevel_8', 'Pike_Level_8', 'SpearLevel_8', 'SwordRangLevel_8', 
    'ThornLevel_8', 'WindBladeLevel_8', 'WormGlandLevel_8', 'FireRingLevel_1', 
    'FireRingLevel_5', 'FireRingLevel_7', 'KunaiLevel_5', 'MagicWandLevel_5', 
    'PikeLevel_5', 'ShurikenLevel_5', 'SpearLevel_1', 'SpearLevel_5', 'StaffOfStorm_Level3', 
    'ThornLevel_1', 'ThunderStaffLevel_1', 'ThunderStaffLevel_5', 'Weapon_Count_3', 
    'Weapon_MaxLevel', 'Weapon_MaxLevel_2', 'Weapon_MaxLevel_3', 'Weapon_MaxLevel_4', 
    'WindBladeLevel_5', 'Attack_Speed_slow_1', 'Corruption_1', 'Corruption_100', 
    'Corruption_20', 'Corruption_5', 'Corruption_50', 'Purification_20', 'CriticalChance_1', 
    'CriticalChance_2', 'CriticalChance_3', 'CriticalChance_4', 'CriticalDamage_1', 
    'CriticalDamage_2', 'Damage_1', 'Damage_2', 'Damage_3', 'Damage_4', 'Damage_5', 
    'Damage_6', 'Damage_Negative', 'Power_7', 'Dash_1', 'Dash_2', 'Dash_3', 'Dash_CD_1', 
    'Dash_CD_2', 'DefencePiercing_1', 'DefencePiercing_2', 'DefencePiercing_3', 
    'DefencePiercing_4', 'DefenceShredding_1', 'DefenceShredding_2', 'DefenceShredding_3', 
    'DefenceShredding_4', 'Damage_Mitigation_1', 'Damage_Mitigation_2', 'Damage_Mitigation_3', 
    'Damage_Mitigation_4', 'Defence_1', 'Defence_2', 'Defence_3', 'Defence_4', 'Defence_5', 
    'Defence_6', 'Defence_7', 'Negative_Defence_1', 'Negative_Defence_2', 'Negative_Defence_3', 
    'FireWork', 'Health_1', 'Health_2', 'Health_3', 'Health_4', 'Health_5', 'Health_6', 
    'Health_Regen_1', 'Health_Regen_2', 'Health_Regen_3', 'KnockBack_1', 
    'MoonCardDropChance_1', 'Move_Speed_1', 'Move_Speed_2', 'Move_Speed_3', 'Pick_Up_Range', 
    'Pick_Up_Range_2', 'Piercing_35', 'PLifeTime_1', 'PSize_1', 'PSize_2', 'PSpeed_1', 
    'PSpeed_2', 'PSpeed_3', 'PSpeed_4', 'Slow_Move_Speed_1', 'Talent_Charge_Cost_1', 
    'Talent_Charge_Multiplier_1', 'Talent_Charge_Rate_1', 'Talent_Charge_Rate_2', 
    'Talent_Max_Charge_1', 'Talent_Power_1', 'Talent_Power_2', 'Talent_Power_3', 
    'Talent_Power_4', 'XPMultiplier_1', 'XPMultiplier_Negative_1', 'Finish_B_50Min', 
    'Finish_C_45Min', 'Finish_D_35Min', 'Finish_E_20Min', 'Finish_F_10Min', 'Reach_10Min', 
    'Reach_30Min_E', 'Reach_40Min_C', 'Reach_45Min_D', 'Food_1', 'Food_2', 'Food_3', 
    'VoidAndFood', 'Kill_Boss_A1', 'Kill_Boss_A2', 'Kill_Boss_A3', 'Kill_Boss_A4', 
    'Kill_Boss_A5', 'Kill_Boss_A6', 'Kill_Boss_B1', 'Kill_Boss_B2', 'Kill_Boss_B3', 
    'Kill_Boss_B4', 'Kill_Boss_B5', 'Kill_Boss_C1', 'Kill_Boss_C2', 'Kill_Boss_C3', 
    'Kill_Boss_C4', 'Kill_Boss_D1', 'Kill_Boss_D2', 'Kill_Boss_D3', 'Kill_Boss_E1', 
    'Kill_Boss_E2', 'Kill_Boss_F1', 'Kill_Elite_1', 'Kill_Elite_2', 'Kill_Elite_3', 
    'Kill_Elite_4', 'Kill_Elite_5', 'Kill_Elite_6', 'Kill_Monster_100', 'Kill_Monster_100k', 
    'Kill_Monster_10k', 'Kill_Monster_10m', 'Kill_Monster_1k', 'Kill_Monster_1m', 
    'Kill_Possesed_Candelabra', 'Kill_ProtectiveSpirit', 'Dried_Mushroom_Unlock', 
    'Giant_Worm_Summon_Weapon_Unlock', 'Goblin_Shaman_Summon_Weapon_Unlock', 
    'Necromancer_Summon_Weapon_Unlock', 'Goblin_Hand_Unlock', 'Hard_Leather_Unlock', 
    'Light_Crystal_Unlock', 'Long_Nail_Unlock', 'Pharaon_Mask_Unlock', 'Red_Skull_Unlock', 
    'Weightless_Crystal_Unlock', 'Wind_Feather_Unlock', 'Bestiary_Completion_Achievement_01', 
    'Bestiary_Completion_Achievement_10', 'Bestiary_Completion_Achievement_20', 
    'Bestiary_Completion_Achievement_30', 'Bestiary_Completion_Achievement_50', 
    'Bestiary_Completion_Achievement_75', 'Bestiary_Completion_Achievement_90', 'death_10', 
    'death_2', 'death_20', 'death_30', 'death_5', 'Game_Count_1', 'Game_Count_10', 
    'Game_Count_20', 'Game_Count_5', 'Game_Count_50', '100kglobalgold', '10kglobalgold', 
    '10kgold', '10ktotalgold', '10mglobalgold', '1mglobalgold', '1Mtotalgold', '200kgold', 
    'KillTarget_ArcaneBeam', 'KillTarget_BloodSyphoon', 'KillTarget_Bow', 'KillTarget_Cleaver', 
    'KillTarget_Crossbow', 'KillTarget_CrystalSword', 'KillTarget_DeathAura', 
    'KillTarget_ExplosiveVial', 'KillTarget_FIreRing', 'KillTarget_IceNova', 
    'KillTarget_Katana', 'KillTarget_Kunai', 'KillTarget_MagicWand', 'KillTarget_MagicWisp', 
    'KillTarget_Pike', 'KillTarget_ShamanStaff', 'KillTarget_Shuriken', 'KillTarget_Spear', 
    'KillTarget_Swordrang', 'KillTarget_Thorn', 'KillTarget_ThrowingKnife', 
    'KillTarget_ThunderStaff', 'KillTarget_WindBlade', 'KillTarget_WormGland', 
    'AltarCorruption', 'BanishCard', 'BTGR_Achievement', 'EvenGodCanBleed', 'AntiHero', 
    'BreakMirror', 'CommonerHero', 'CrystalCraft', 'GoblinWorkforce', 'Golden_Idol', 
    'ShopKeeperBestFriend', 'SomethingTerriblyWrong', 'SongOfConquest', 'SongOfSouls', 
    'SongOfTheMighty', 'SongOfTheSlayer', 'SongOfTheWealthy', 'GettingScammed', 
    'IllegalMove', 'Kill_Unkillable', 'LV99MafiaBoss', 'PhaseSkipper', 'SixtyFour', 
    'SlideShow', 'Card_Fire_2', 'Card_Moon_1', 'Card_Moon_2', 'DamageTaken', 
    'DamageTaken_2', 'DamageTaken_3', 'Invested_10M', 'Invested_1M', 'All7Sins', 
    'EnvyAchievement', 'GluttonyAchievement', 'GreedAchievement', 'LustAchievement', 
    'PrideAchievement', 'SlothAchievement', 'WrathAchievement', 'AntiEquipment', 
    'DecentEquipment', 'GettingTheGoodStuff', 'ToInfinityAndBeyond', 'Ach_A_BloodHanded', 
    'Ach_A_Pacifist', 'Ach_A_Purist', 'Ach_A_Rooted', 'Ach_A_RootedCubed', 'Ach_A_Souless', 
    'Ach_A_Vanilla', 'Ach_B_Arcade', 'Ach_B_DwindlingFire', 'Ach_B_MortalSoul', 
    'Ach_B_Overgeared', 'Ach_B_TimeParadox', 'C_ArmorBan', 'C_FastPass', 
    'C_LeftImpariment_Ach', 'C_RiskOfStorm', 'C_ShopKeeperVacationEnd', 'C_VildCurse', 
    'D_Cursed', 'D_ElentorScalingHell_Corrupted', 'D_Hell', 'D_NoShop', 'D_Peasant', 
    'D_SoulLess', 'D_Tainted', 'D_TwoWeapon', 'Surv_C_KillThemUp', 'Surv_D_HourGlass', 
    'E_BrokenWeapon', 'E_NoShop', 'E_Peasant', 'E_Plex_Hard', 'E_Sick', 'E_Sifd', 
    'E_SoulLess', 'E_Tainted', 'Surv_E_ChaoticPlayground', 'F_NoShop', 'F_Peasant', 
    'F_Sick', 'F_SingleArmed', 'F_Snuff', 'F_Snuff_Duelist', 'F_SoulLess', 'F_Tainted', 
    'F_True_Snuff', 'Surv_F_BoneGlass', 'Challenge_CompleteAllARankHardmodeChallenges', 
    'Challenge_CompleteARankChallengeExpert', 'Challenge_Completion_1', 
    'Challenge_Completion_2', 'Challenge_Completion_3', 'Challenge_Completion_4', 
    'Challenge_UnlockHardMode', 'Ach_S_ExperienceLeak', 'Ach_S_LevelScaling', 
    'Ach_S_TabulaRasa', 'GettingReady', 'SL_100', 'SL_1000', 'SL_20', 'SL_250', 
    'SL_50', 'SL_500', 'SL_Cap'
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_game_profiles():
    base_path = os.path.expandvars(r"%USERPROFILE%\AppData\LocalLow\HuardOuadi\Rogue Genesia\Profile")
    if not os.path.exists(base_path):
        return None
    profiles = [f for f in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, f))]
    return base_path, profiles

def backup_file(file_path):
    if os.path.exists(file_path):
        backup_path = file_path + ".bak"
        shutil.copy2(file_path, backup_path)
        return True
    return False

def change_soulcoin(data):
    print("\n--- Change SoulCoin ---")
    if "SoulCoin" in data:
        print(f"Current SoulCoin: {data['SoulCoin']}")
    else:
        print("SoulCoin not found in the save file. We will create it.")
    
    while True:
        user_input = input("\nEnter new amount of SoulCoins (or 'c' to cancel): ")
        if user_input.lower() == 'c':
            return False
        try:
            new_amount = float(user_input)
            if new_amount < 0:
                print("Error: Cannot be negative.")
                continue
            data["SoulCoin"] = new_amount
            print(f"\n[SUCCESS] SoulCoin set to {new_amount}!")
            return True
        except ValueError:
            print("[ERROR] Invalid input.")

def manage_avatars(data):
    if "AvatarSave" not in data:
        print("\n[ERROR] 'AvatarSave' not found.")
        return False
        
    was_changed = False
    while True:
        clear_screen()
        print("====================================")
        print("          UNLOCK AVATARS            ")
        print("====================================")
        
        avatars = data["AvatarSave"]
        display_list = [av for av in avatars if av.get("Localisation_Name") != "RogKnight"]
                
        for i, av in enumerate(display_list, 1):
            status = "UNLOCKED" if av.get("Unlocked") else "Locked"
            print(f"[{i}] {av.get('Localisation_Name', 'Unknown').ljust(20)} - {status}")
            
        lock_all_idx = len(display_list) + 1
        print("------------------------------------")
        print(f"[{lock_all_idx}] Lock All (Except RogKnight)")
        print("[0] Done / Back")
        print("====================================")
        
        choice = input("Select an option: ")
        if choice == '0':
            return was_changed
        elif choice == str(lock_all_idx):
            for av in avatars:
                av["Unlocked"] = (av.get("Localisation_Name") == "RogKnight")
            print("\n[SUCCESS] Avatars locked!")
            was_changed = True
            input("Press Enter to continue...")
        else:
            try:
                idx = int(choice)
                if 1 <= idx <= len(display_list):
                    selected_av = display_list[idx - 1]
                    if not selected_av.get("Unlocked"):
                        selected_av["Unlocked"] = True
                        was_changed = True
                        print(f"\n[SUCCESS] {selected_av.get('Localisation_Name')} UNLOCKED!")
                    else:
                        print("\nAlready unlocked.")
                    input("Press Enter to continue...")
            except ValueError:
                print("\n[ERROR] Invalid number.")
                time.sleep(1)

def manage_challenges(data):
    if "Challenges" not in data:
        print("\n[ERROR] 'Challenges' not found.")
        return False

    was_changed = False
    while True:
        clear_screen()
        print("====================================")
        print("         MANAGE CHALLENGES          ")
        print("====================================")
        print("[1] Unlock All Challenges")
        print("[2] Lock All Challenges")
        print("[0] Done / Back")
        print("====================================")

        choice = input("Select an option: ")
        if choice == '0':
            return was_changed
        elif choice == '1':
            for ch in data["Challenges"]:
                ch["Completed"] = True
                ch["Viewed"] = True
                ch["MaximumCompletionLevel"] = ch.get("MaximumAvailableLevel", 1)
            print("\n[SUCCESS] Challenges marked COMPLETED!")
            was_changed = True
            input("Press Enter to continue...")
        elif choice == '2':
            for ch in data["Challenges"]:
                ch["Completed"] = False
                ch["MaximumCompletionLevel"] = 0
            print("\n[SUCCESS] Challenges RESET!")
            was_changed = True
            input("Press Enter to continue...")
        else:
            print("\n[ERROR] Invalid.")
            time.sleep(1)

def set_materials(data):
    print("\n--- Set Materials ---")
    if "Materials" not in data or not isinstance(data["Materials"], dict):
        data["Materials"] = {}

    while True:
        user_input = input("\nEnter amount for all 14 materials (1 - 10000) or 'c' to cancel: ")
        if user_input.lower() == 'c':
            return False
        try:
            new_amount = float(user_input)
            if not 1 <= new_amount <= 10000:
                print("[ERROR] Must be between 1 and 10000.")
                continue
            for i in range(1, 15):
                data["Materials"][str(i)] = new_amount
            print(f"\n[SUCCESS] Materials set to {new_amount}!")
            return True
        except ValueError:
            print("[ERROR] Invalid input.")

def manage_achievements(ach_file_path):
    while True:
        clear_screen()
        print("====================================")
        print("        MANAGE ACHIEVEMENTS         ")
        print("  **This feature is still in beta** ")
        print(" and currently misses 4 achievements")
        print("====================================")
        print("[1] Unlock ALL Achievements")
        print("[2] Reset (Lock) ALL Achievements")
        print("[0] Done / Back")
        print("====================================")
        
        choice = input("Select an option: ")
        if choice == '0':
            break
            
        if choice in ['1', '2']:
            backup_file(ach_file_path)
            data = {"AchievementSaves": []}
            
            if os.path.exists(ach_file_path):
                try:
                    with open(ach_file_path, 'r', encoding='utf-8') as f:
                        data = json.loads(base64.b64decode(f.read().strip()).decode('utf-8'))
                    if "AchievementSaves" not in data:
                        data["AchievementSaves"] = []
                except Exception:
                    print("\n[WARNING] Failed to parse existing file. Creating new structure.")
                
            if choice == '1':
                data["AchievementSaves"] = [{"AchievementID": a, "unlocked": True, "unlockTime": 0} for a in MASTER_ACHIEVEMENTS]
                print(f"\n[SUCCESS] Unlocked ALL {len(MASTER_ACHIEVEMENTS)} Achievements!")
            elif choice == '2':
                data["AchievementSaves"] = []
                print("\n[SUCCESS] All achievements RESET!")
            
            try:
                with open(ach_file_path, 'w', encoding='utf-8') as f:
                    f.write(base64.b64encode(json.dumps(data, indent=2).encode('utf-8')).decode('utf-8'))
            except Exception as e:
                print(f"\n[ERROR] Failed to save: {e}")
                
            input("\nPress Enter to continue...")

def select_profile():
    result = get_game_profiles()
    if not result or not result[1]:
        print("[ERROR] Could not find Rogue Genesia profiles folder.")
        print(r"Expected path: %USERPROFILE%\AppData\LocalLow\HuardOuadi\Rogue Genesia\Profile")
        input("Press Enter to exit...")
        return None

    base_path, profiles = result
    
    while True:
        clear_screen()
        print("====================================")
        print("          SELECT PROFILE            ")
        print("====================================")
        for i, p in enumerate(profiles, 1):
            print(f"[{i}] {p}")
        print("[0] Exit Program")
        print("====================================")
        
        choice = input("Enter profile number: ")
        if choice == '0':
            return None
            
        try:
            idx = int(choice)
            if 1 <= idx <= len(profiles):
                return os.path.join(base_path, profiles[idx-1])
        except ValueError:
            pass
            
        print("Invalid choice.")
        time.sleep(1)

def main():
    target_dir = select_profile()
    if not target_dir:
        return

    save_file = os.path.join(target_dir, "PersistantSave.rgsav")
    ach_file = os.path.join(target_dir, "Achievements.rgsav")

    print("\n[INFO] Backing up save files...")
    backup_save = backup_file(save_file)
    backup_ach = backup_file(ach_file)
    print(f"PersistantSave backup: {'Created' if backup_save else 'Not Found'}")
    print(f"Achievements backup: {'Created' if backup_ach else 'Not Found'}")
    time.sleep(2)

    while True:
        clear_screen()
        print("====================================")
        print("          DABSHIAN-ROGUE            ")
        print("        Developed by MeyTiii        ")
        print("====================================")
        print(f"Active Profile: {os.path.basename(target_dir)}")
        print("------------------------------------")
        print("[1] Change SoulCoin amount")
        print("[2] Manage Avatars")
        print("[3] Manage Challenges")
        print("[4] Set Materials")
        print("[5] Manage Achievements")
        print("[0] Exit")
        print("====================================")

        choice = input("Select an option: ")
        if choice == '0':
            break
            
        elif choice == '5':
            manage_achievements(ach_file)
            
        elif choice in ['1', '2', '3', '4']:
            if not os.path.exists(save_file):
                print(f"\n[ERROR] Save file not found in profile.")
                input("\nPress Enter to continue...")
                continue
            
            try:
                with open(save_file, 'r', encoding='utf-8') as f:
                    data = json.loads(base64.b64decode(f.read().strip()).decode('utf-8'))
            except Exception:
                print("\n[ERROR] Failed to read or decode the save file.")
                input("\nPress Enter to continue...")
                continue
                
            was_changed = False
            if choice == '1': was_changed = change_soulcoin(data)
            elif choice == '2': was_changed = manage_avatars(data)
            elif choice == '3': was_changed = manage_challenges(data)
            elif choice == '4': was_changed = set_materials(data)
            
            if was_changed:
                try:
                    with open(save_file, 'w', encoding='utf-8') as f:
                        f.write(base64.b64encode(json.dumps(data, indent=2).encode('utf-8')).decode('utf-8'))
                    print("Save file successfully updated!")
                except Exception as e:
                    print(f"\n[ERROR] Failed to save: {e}")
            
            if choice in ['1', '4']:
                input("\nPress Enter to return to menu...")

if __name__ == "__main__":
    main()