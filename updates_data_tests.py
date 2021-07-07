"""Statify update_datebase tests"""

tracks = [{'album': {'album_type': 'ALBUM', 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/1VPmR4DJC1PlOtd0IADAO0'}, 'href': 'https://api.spotify.com/v1/artists/1VPmR4DJC1PlOtd0IADAO0', 'id': '1VPmR4DJC1PlOtd0IADAO0', 'name': '$uicideboy$', 'type': 'artist', 'uri': 'spotify:artist:1VPmR4DJC1PlOtd0IADAO0'}], 'available_markets': ['AD', 'AE', 'AR', 'AT', 'AU', 'BE', 'BG', 'BH', 'BO', 'BR', 'CA', 'CH', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'FI', 'FR', 'GB', 'GR', 'GT', 'HK', 'HN', 'HU', 'ID', 'IE', 'IL', 'IN', 'IS', 'IT', 'JO', 'JP', 'KW', 'LB', 'LI', 'LT', 'LU', 'LV', 'MA', 'MC', 'MT', 'MX', 'MY', 'NI', 'NL', 'NO', 'NZ', 'OM', 'PA', 'PE', 'PH', 'PL', 'PS', 'PT', 'PY', 'QA', 'RO', 'SA', 'SE', 'SG', 'SK', 'SV', 'TH', 'TN', 'TR', 'TW', 'US', 'UY', 'VN', 'ZA'], 'external_urls': {'spotify': 'https://open.spotify.com/album/2ivOxIKDHxEo6WMD9m3ytn'}, 'href': 'https://api.spotify.com/v1/albums/2ivOxIKDHxEo6WMD9m3ytn', 'id': '2ivOxIKDHxEo6WMD9m3ytn', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b2739db03c8368f127291ced4263', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e029db03c8368f127291ced4263', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d000048519db03c8368f127291ced4263', 'width': 64}], 'name': 'I Want to Die In New Orleans', 'release_date': '2018-09-07', 'release_date_precision': 'day', 'total_tracks': 14, 'type': 'album', 'uri': 'spotify:album:2ivOxIKDHxEo6WMD9m3ytn'}, 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/1VPmR4DJC1PlOtd0IADAO0'}, 'href': 'https://api.spotify.com/v1/artists/1VPmR4DJC1PlOtd0IADAO0', 'id': '1VPmR4DJC1PlOtd0IADAO0', 'name': '$uicideboy$', 'type': 'artist', 'uri': 'spotify:artist:1VPmR4DJC1PlOtd0IADAO0'}], 'available_markets': ['AD', 'AE', 'AR', 'AT', 'AU', 'BE', 'BG', 'BH', 'BO', 'BR', 'CA', 'CH', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'FI', 'FR', 'GB', 'GR', 'GT', 'HK', 'HN', 'HU', 'ID', 'IE', 'IL', 'IN', 'IS', 'IT', 'JO', 'JP', 'KW', 'LB', 'LI', 'LT', 'LU', 'LV', 'MA', 'MC', 'MT', 'MX', 'MY', 'NI', 'NL', 'NO', 'NZ', 'OM', 'PA', 'PE', 'PH', 'PL', 'PS', 'PT', 'PY', 'QA', 'RO', 'SA', 'SE', 'SG', 'SK', 'SV', 'TH', 'TN', 'TR', 'TW', 'US', 'UY', 'VN', 'ZA'], 'disc_number': 1, 'duration_ms': 185217, 'explicit': True, 'external_ids': {'isrc': 'QZAPK1700030'}, 'external_urls': {'spotify': 'https://open.spotify.com/track/6cpslq4nypOt9NhLPIwY6c'}, 'href': 'https://api.spotify.com/v1/tracks/6cpslq4nypOt9NhLPIwY6c', 'id': '6cpslq4nypOt9NhLPIwY6c', 'is_local': False, 'name': 'King Tulip', 'popularity': 62, 'preview_url': 'https://p.scdn.co/mp3-preview/298023ae45267e3b8cfc717ecddf56ff037f6213?cid=7c396993dafd46c3b30341981ec56217', 'track_number': 1, 'type': 'track', 'uri': 'spotify:track:6cpslq4nypOt9NhLPIwY6c'}, {'album': {'album_type': 'ALBUM', 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4'}, 'href': 'https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4', 'id': '3TVXtAsR1Inumwj472S9r4', 'name': 'Drake', 'type': 'artist', 'uri': 'spotify:artist:3TVXtAsR1Inumwj472S9r4'}], 'available_markets': ['AD', 'AE', 'AR', 'AT', 'AU', 'BE', 'BG', 'BH', 'BO', 'BR', 'CA', 'CH', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'FI', 'FR', 'GB', 'GR', 'GT', 'HK', 'HN', 'HU', 'ID', 'IE', 'IL', 'IS', 'IT', 'JO', 'JP', 'KW', 'LB', 'LI', 'LT', 'LU', 'LV', 'MA', 'MC', 'MT', 'MX', 'MY', 'NI', 'NL', 'NO', 'NZ', 'OM', 'PA', 'PE', 'PH', 'PL', 'PT', 'PY', 'QA', 'RO', 'SA', 'SE', 'SG', 'SK', 'SV', 'TH', 'TN', 'TR', 'TW', 'US', 'UY', 'VN', 'ZA'], 'external_urls': {'spotify': 'https://open.spotify.com/album/40GMAhriYJRO1rsY4YdrZb'}, 'href': 'https://api.spotify.com/v1/albums/40GMAhriYJRO1rsY4YdrZb', 'id': '40GMAhriYJRO1rsY4YdrZb', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b2739416ed64daf84936d89e671c', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e029416ed64daf84936d89e671c', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d000048519416ed64daf84936d89e671c', 'width': 64}], 'name': 'Views', 'release_date': '2016-05-06', 'release_date_precision': 'day', 'total_tracks': 20, 'type': 'album', 'uri': 'spotify:album:40GMAhriYJRO1rsY4YdrZb'}, 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4'}, 'href': 'https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4', 'id': '3TVXtAsR1Inumwj472S9r4', 'name': 'Drake', 'type': 'artist', 'uri': 'spotify:artist:3TVXtAsR1Inumwj472S9r4'}], 'available_markets': ['AD', 'AE', 'AR', 'AT', 'AU', 'BE', 'BG', 'BH', 'BO', 'BR', 'CA', 'CH', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'FI', 'FR', 'GB', 'GR', 'GT', 'HK', 'HN', 'HU', 'ID', 'IE', 'IL', 'IS', 'IT', 'JO', 'JP', 'KW', 'LB', 'LI', 'LT', 'LU', 'LV', 'MA', 'MC', 'MT', 'MX', 'MY', 'NI', 'NL', 'NO', 'NZ', 'OM', 'PA', 'PE', 'PH', 'PL', 'PT', 'PY', 'QA', 'RO', 'SA', 'SE', 'SG', 'SK', 'SV', 'TH', 'TN', 'TR', 'TW', 'US', 'UY', 'VN', 'ZA'], 'disc_number': 1, 'duration_ms': 189853, 'explicit': True, 'external_ids': {'isrc': 'USCM51600078'}, 'external_urls': {'spotify': 'https://open.spotify.com/track/433P7tDcIAi6NLnf4Sh6tI'}, 'href': 'https://api.spotify.com/v1/tracks/433P7tDcIAi6NLnf4Sh6tI', 'id': '433P7tDcIAi6NLnf4Sh6tI', 'is_local': False, 'name': 'Still Here', 'popularity': 67, 'preview_url': 'https://p.scdn.co/mp3-preview/0105a85f6f672de5b4ab8d7cfdf17bbcdff02df3?cid=7c396993dafd46c3b30341981ec56217', 'track_number': 10, 'type': 'track', 'uri': 'spotify:track:433P7tDcIAi6NLnf4Sh6tI'}, {'album': {'album_type': 'ALBUM', 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/1VPmR4DJC1PlOtd0IADAO0'}, 'href': 'https://api.spotify.com/v1/artists/1VPmR4DJC1PlOtd0IADAO0', 'id': '1VPmR4DJC1PlOtd0IADAO0', 'name': '$uicideboy$', 'type': 'artist', 'uri': 'spotify:artist:1VPmR4DJC1PlOtd0IADAO0'}], 'available_markets': ['AD', 'AE', 'AR', 'AT', 'AU', 'BE', 'BG', 'BH', 'BO', 'BR', 'CA', 'CH', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'FI', 'FR', 'GB', 'GR', 'GT', 'HK', 'HN', 'HU', 'ID', 'IE', 'IL', 'IN', 'IS', 'IT', 'JO', 'JP', 'KW', 'LB', 'LI', 'LT', 'LU', 'LV', 'MA', 'MC', 'MT', 'MX', 'MY', 'NI', 'NL', 'NO', 'NZ', 'OM', 'PA', 'PE', 'PH', 'PL', 'PS', 'PT', 'PY', 'QA', 'RO', 'SA', 'SE', 'SG', 'SK', 'SV', 'TH', 'TN', 'TR', 'TW', 'US', 'UY', 'VN', 'ZA'], 'external_urls': {'spotify': 'https://open.spotify.com/album/1aVnxqszPG45yn2nFsVQRS'}, 'href': 'https://api.spotify.com/v1/albums/1aVnxqszPG45yn2nFsVQRS', 'id': '1aVnxqszPG45yn2nFsVQRS', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b2738abb1b7abadd031c551aaa8c', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e028abb1b7abadd031c551aaa8c', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d000048518abb1b7abadd031c551aaa8c', 'width': 64}], 'name': 'Grey Sheep II', 'release_date': '2016-05-25', 'release_date_precision': 'day', 'total_tracks': 7, 'type': 'album', 'uri': 'spotify:album:1aVnxqszPG45yn2nFsVQRS'}, 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/1VPmR4DJC1PlOtd0IADAO0'}, 'href': 'https://api.spotify.com/v1/artists/1VPmR4DJC1PlOtd0IADAO0', 'id': '1VPmR4DJC1PlOtd0IADAO0', 'name': '$uicideboy$', 'type': 'artist', 'uri': 'spotify:artist:1VPmR4DJC1PlOtd0IADAO0'}], 'available_markets': ['AD', 'AE', 'AR', 'AT', 'AU', 'BE', 'BG', 'BH', 'BO', 'BR', 'CA', 'CH', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'FI', 'FR', 'GB', 'GR', 'GT', 'HK', 'HN', 'HU', 'ID', 'IE', 'IL', 'IN', 'IS', 'IT', 'JO', 'JP', 'KW', 'LB', 'LI', 'LT', 'LU', 'LV', 'MA', 'MC', 'MT', 'MX', 'MY', 'NI', 'NL', 'NO', 'NZ', 'OM', 'PA', 'PE', 'PH', 'PL', 'PS', 'PT', 'PY', 'QA', 'RO', 'SA', 'SE', 'SG', 'SK', 'SV', 'TH', 'TN', 'TR', 'TW', 'US', 'UY', 'VN', 'ZA'], 'disc_number': 1, 'duration_ms': 118073, 'explicit': True, 'external_ids': {'isrc': 'QM8DG1600831'}, 'external_urls': {'spotify': 'https://open.spotify.com/track/1hSBVYwG0UPeou0ORftrxm'}, 'href': 'https://api.spotify.com/v1/tracks/1hSBVYwG0UPeou0ORftrxm', 'id': '1hSBVYwG0UPeou0ORftrxm', 'is_local': False, 'name': 'Do You Believe in God?', 'popularity': 64, 'preview_url': 'https://p.scdn.co/mp3-preview/1953f3e8daa9a8fa868d7a34d67dd60f42785f45?cid=7c396993dafd46c3b30341981ec56217', 'track_number': 1, 'type': 'track', 'uri': 'spotify:track:1hSBVYwG0UPeou0ORftrxm'}, {'album': {'album_type': 'SINGLE', 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/1VPmR4DJC1PlOtd0IADAO0'}, 'href': 'https://api.spotify.com/v1/artists/1VPmR4DJC1PlOtd0IADAO0', 'id': '1VPmR4DJC1PlOtd0IADAO0', 'name': '$uicideboy$', 'type': 'artist', 'uri': 'spotify:artist:1VPmR4DJC1PlOtd0IADAO0'}], 'available_markets': ['AD', 'AE', 'AR', 'AT', 'AU', 'BE', 'BG', 'BH', 'BO', 'BR', 'CA', 'CH', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'FI', 'FR', 'GB', 'GR', 'GT', 'HK', 'HN', 'HU', 'ID', 'IE', 'IL', 'IN', 'IS', 'IT', 'JO', 'JP', 'KW', 'LB', 'LI', 'LT', 'LU', 'LV', 'MA', 'MC', 'MT', 'MX', 'MY', 'NI', 'NL', 'NO', 'NZ', 'OM', 'PA', 'PE', 'PH', 'PL', 'PS', 'PT', 'PY', 'QA', 'RO', 'SA', 'SE', 'SG', 'SK', 'SV', 'TH', 'TN', 'TR', 'TW', 'US', 'UY', 'VN', 'ZA'], 'external_urls': {'spotify': 'https://open.spotify.com/album/4CcyRnFW6Vgf372ca3xFGR'}, 'href': 'https://api.spotify.com/v1/albums/4CcyRnFW6Vgf372ca3xFGR', 'id': '4CcyRnFW6Vgf372ca3xFGR', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b273f795a2962820664b4112901e', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e02f795a2962820664b4112901e', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d00004851f795a2962820664b4112901e', 'width': 64}], 'name': 'For the Last Time', 'release_date': '2017-09-05', 'release_date_precision': 
'day', 'total_tracks': 1, 'type': 'album', 'uri': 'spotify:album:4CcyRnFW6Vgf372ca3xFGR'}, 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/1VPmR4DJC1PlOtd0IADAO0'}, 'href': 'https://api.spotify.com/v1/artists/1VPmR4DJC1PlOtd0IADAO0', 'id': '1VPmR4DJC1PlOtd0IADAO0', 'name': '$uicideboy$', 'type': 'artist', 'uri': 'spotify:artist:1VPmR4DJC1PlOtd0IADAO0'}], 'available_markets': ['AD', 'AE', 'AR', 'AT', 'AU', 'BE', 'BG', 'BH', 'BO', 'BR', 'CA', 'CH', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'FI', 'FR', 'GB', 'GR', 'GT', 'HK', 'HN', 'HU', 'ID', 'IE', 'IL', 'IN', 'IS', 'IT', 'JO', 'JP', 'KW', 'LB', 'LI', 'LT', 'LU', 'LV', 'MA', 'MC', 'MT', 'MX', 'MY', 'NI', 'NL', 'NO', 'NZ', 'OM', 'PA', 'PE', 'PH', 'PL', 'PS', 'PT', 'PY', 'QA', 'RO', 'SA', 'SE', 'SG', 'SK', 'SV', 'TH', 'TN', 'TR', 'TW', 'US', 'UY', 'VN', 'ZA'], 'disc_number': 1, 'duration_ms': 156081, 'explicit': True, 'external_ids': {'isrc': 'QM8DG1703420'}, 'external_urls': {'spotify': 'https://open.spotify.com/track/240audWazVjwvwh7XwfSZE'}, 'href': 'https://api.spotify.com/v1/tracks/240audWazVjwvwh7XwfSZE', 'id': '240audWazVjwvwh7XwfSZE', 'is_local': False, 'name': 'For the Last Time', 'popularity': 71, 'preview_url': 'https://p.scdn.co/mp3-preview/ca215d2a7747b6ac421d1a193f5013328a7c4e51?cid=7c396993dafd46c3b30341981ec56217', 'track_number': 1, 'type': 'track', 'uri': 'spotify:track:240audWazVjwvwh7XwfSZE'}, {'album': {'album_type': 'ALBUM', 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/1VPmR4DJC1PlOtd0IADAO0'}, 'href': 'https://api.spotify.com/v1/artists/1VPmR4DJC1PlOtd0IADAO0', 'id': '1VPmR4DJC1PlOtd0IADAO0', 'name': '$uicideboy$', 'type': 'artist', 'uri': 'spotify:artist:1VPmR4DJC1PlOtd0IADAO0'}], 'available_markets': ['AD', 'AE', 'AR', 'AT', 'AU', 'BE', 'BG', 'BH', 'BO', 'BR', 'CA', 'CH', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'FI', 'FR', 'GB', 'GR', 'GT', 'HK', 'HN', 'HU', 'ID', 'IE', 'IL', 'IN', 'IS', 'IT', 'JO', 'JP', 'KW', 'LB', 'LI', 'LT', 'LU', 'LV', 'MA', 'MC', 'MT', 'MX', 'MY', 'NI', 'NL', 'NO', 'NZ', 'OM', 'PA', 'PE', 'PH', 'PL', 'PS', 'PT', 'PY', 'QA', 'RO', 'SA', 'SE', 'SG', 'SK', 'SV', 'TH', 'TN', 'TR', 'TW', 'US', 'UY', 'VN', 'ZA'], 'external_urls': {'spotify': 'https://open.spotify.com/album/4BqLJSu0S1KEsA6DBbJ9L4'}, 'href': 'https://api.spotify.com/v1/albums/4BqLJSu0S1KEsA6DBbJ9L4', 'id': '4BqLJSu0S1KEsA6DBbJ9L4', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b2732417400ddf7445276814eeb6', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e022417400ddf7445276814eeb6', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d000048512417400ddf7445276814eeb6', 'width': 64}], 'name': '7th or St. Tammany', 'release_date': '2015-04-02', 'release_date_precision': 'day', 'total_tracks': 12, 'type': 'album', 'uri': 'spotify:album:4BqLJSu0S1KEsA6DBbJ9L4'}, 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/1VPmR4DJC1PlOtd0IADAO0'}, 'href': 'https://api.spotify.com/v1/artists/1VPmR4DJC1PlOtd0IADAO0', 'id': '1VPmR4DJC1PlOtd0IADAO0', 'name': '$uicideboy$', 'type': 'artist', 'uri': 'spotify:artist:1VPmR4DJC1PlOtd0IADAO0'}], 'available_markets': ['AD', 'AE', 'AR', 'AT', 'AU', 'BE', 'BG', 'BH', 'BO', 'BR', 'CA', 'CH', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'FI', 'FR', 'GB', 'GR', 'GT', 'HK', 'HN', 'HU', 'ID', 'IE', 'IL', 'IN', 'IS', 'IT', 'JO', 'JP', 'KW', 'LB', 'LI', 'LT', 'LU', 'LV', 'MA', 'MC', 'MT', 'MX', 'MY', 'NI', 'NL', 'NO', 'NZ', 'OM', 'PA', 'PE', 'PH', 'PL', 'PS', 'PT', 'PY', 'QA', 'RO', 'SA', 'SE', 'SG', 'SK', 'SV', 'TH', 'TN', 'TR', 'TW', 'US', 'UY', 'VN', 'ZA'], 'disc_number': 1, 'duration_ms': 143220, 'explicit': True, 'external_ids': {'isrc': 'QM8DG1600593'}, 'external_urls': {'spotify': 'https://open.spotify.com/track/00UDmkyejOcUApEqpiB90i'}, 'href': 'https://api.spotify.com/v1/tracks/00UDmkyejOcUApEqpiB90i', 'id': '00UDmkyejOcUApEqpiB90i', 'is_local': False, 'name': 'Dead Batteries', 'popularity': 66, 'preview_url': 'https://p.scdn.co/mp3-preview/c57509ca36a35060b3a05155909796c4421f8be3?cid=7c396993dafd46c3b30341981ec56217', 'track_number': 2, 'type': 'track', 'uri': 'spotify:track:00UDmkyejOcUApEqpiB90i'}, {'album': {'album_type': 'SINGLE', 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/5a2w2tgpLwv26BYJf2qYwu'}, 'href': 'https://api.spotify.com/v1/artists/5a2w2tgpLwv26BYJf2qYwu', 'id': '5a2w2tgpLwv26BYJf2qYwu', 'name': 'SOPHIE', 'type': 'artist', 'uri': 'spotify:artist:5a2w2tgpLwv26BYJf2qYwu'}], 'available_markets': ['AD', 'AE', 'AR', 'AT', 'AU', 'BE', 'BG', 'BH', 'BO', 'BR', 'CA', 'CH', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'FI', 'FR', 'GB', 'GR', 'GT', 'HK', 'HN', 'HU', 'ID', 'IE', 'IL', 'IN', 'IS', 'IT', 'JO', 'JP', 'KW', 'LB', 'LI', 'LT', 'LU', 'LV', 'MA', 'MC', 'MT', 'MX', 'MY', 'NI', 'NL', 'NO', 'NZ', 'OM', 'PA', 'PE', 'PH', 'PL', 'PS', 'PT', 'PY', 'QA', 'RO', 'SA', 'SE', 'SG', 'SK', 'SV', 'TH', 'TN', 'TR', 'TW', 'US', 'UY', 'VN', 'ZA'], 'external_urls': {'spotify': 'https://open.spotify.com/album/1Fa53vHM0uwPcjpPOVRM9M'}, 'href': 'https://api.spotify.com/v1/albums/1Fa53vHM0uwPcjpPOVRM9M', 'id': '1Fa53vHM0uwPcjpPOVRM9M', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b273d02ed33304a2a8153ecf12bc', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e02d02ed33304a2a8153ecf12bc', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d00004851d02ed33304a2a8153ecf12bc', 'width': 64}], 'name': 'JUST LIKE WE NEVER SAID GOODBYE', 'release_date': '2015-10-16', 'release_date_precision': 'day', 'total_tracks': 1, 'type': 'album', 'uri': 'spotify:album:1Fa53vHM0uwPcjpPOVRM9M'}, 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/5a2w2tgpLwv26BYJf2qYwu'}, 'href': 'https://api.spotify.com/v1/artists/5a2w2tgpLwv26BYJf2qYwu', 'id': '5a2w2tgpLwv26BYJf2qYwu', 'name': 'SOPHIE', 'type': 'artist', 'uri': 'spotify:artist:5a2w2tgpLwv26BYJf2qYwu'}], 'available_markets': ['AD', 'AE', 'AR', 'AT', 'AU', 'BE', 'BG', 'BH', 'BO', 'BR', 'CA', 'CH', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'FI', 'FR', 'GB', 'GR', 'GT', 'HK', 'HN', 'HU', 'ID', 'IE', 'IL', 'IN', 'IS', 'IT', 'JO', 'JP', 'KW', 'LB', 'LI', 'LT', 'LU', 'LV', 'MA', 'MC', 'MT', 'MX', 'MY', 'NI', 'NL', 'NO', 'NZ', 'OM', 'PA', 'PE', 'PH', 'PL', 'PS', 'PT', 'PY', 'QA', 'RO', 'SA', 'SE', 'SG', 'SK', 'SV', 'TH', 'TN', 'TR', 'TW', 'US', 'UY', 'VN', 'ZA'], 'disc_number': 1, 'duration_ms': 188520, 'explicit': False, 'external_ids': {'isrc': 'GB7CH1500017'}, 'external_urls': {'spotify': 'https://open.spotify.com/track/18yTgk0VgjB9XDj8h2q6Td'}, 'href': 'https://api.spotify.com/v1/tracks/18yTgk0VgjB9XDj8h2q6Td', 'id': '18yTgk0VgjB9XDj8h2q6Td', 'is_local': False, 'name': 'JUST LIKE WE NEVER SAID GOODBYE', 'popularity': 44, 'preview_url': 'https://p.scdn.co/mp3-preview/d5790004de973f83756311075125ffc965e522c8?cid=7c396993dafd46c3b30341981ec56217', 'track_number': 1, 'type': 'track', 'uri': 'spotify:track:18yTgk0VgjB9XDj8h2q6Td'}, {'album': {'album_type': 'ALBUM', 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/4xRYI6VqpkE3UwrDrAZL8L'}, 'href': 'https://api.spotify.com/v1/artists/4xRYI6VqpkE3UwrDrAZL8L', 'id': '4xRYI6VqpkE3UwrDrAZL8L', 'name': 'Logic', 'type': 'artist', 'uri': 'spotify:artist:4xRYI6VqpkE3UwrDrAZL8L'}], 'available_markets': ['AD', 'AE', 'AR', 'AT', 'AU', 'BE', 'BG', 'BH', 'BO', 'BR', 'CA', 'CH', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'FI', 'FR', 'GB', 'GR', 'GT', 'HK', 'HN', 'HU', 'ID', 'IE', 'IL', 'IN', 'IS', 'IT', 'JO', 'JP', 'KW', 'LB', 'LI', 'LT', 'LU', 'LV', 'MA', 'MC', 'MT', 'MX', 'MY', 'NI', 'NL', 'NO', 'NZ', 'OM', 'PA', 'PE', 'PH', 'PL', 'PS', 'PT', 'PY', 'QA', 'RO', 'SA', 'SE', 'SG', 'SK', 'SV', 'TH', 'TN', 'TR', 'TW', 'US', 'UY', 'VN', 'ZA'], 'external_urls': {'spotify': 'https://open.spotify.com/album/3UTazkAlLS4ZmVbIgJentC'}, 'href': 'https://api.spotify.com/v1/albums/3UTazkAlLS4ZmVbIgJentC', 'id': '3UTazkAlLS4ZmVbIgJentC', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b273496ddd69ddb33853f8ff6fb9', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e02496ddd69ddb33853f8ff6fb9', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d00004851496ddd69ddb33853f8ff6fb9', 'width': 64}], 'name': 'YS Collection Vol. 1', 'release_date': '2021-06-25', 'release_date_precision': 'day', 'total_tracks': 14, 'type': 'album', 'uri': 'spotify:album:3UTazkAlLS4ZmVbIgJentC'}, 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/4xRYI6VqpkE3UwrDrAZL8L'}, 'href': 'https://api.spotify.com/v1/artists/4xRYI6VqpkE3UwrDrAZL8L', 'id': '4xRYI6VqpkE3UwrDrAZL8L', 'name': 'Logic', 'type': 'artist', 'uri': 'spotify:artist:4xRYI6VqpkE3UwrDrAZL8L'}], 'available_markets': ['AD', 'AE', 'AR', 'AT', 'AU', 'BE', 'BG', 'BH', 'BO', 'BR', 'CA', 'CH', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'FI', 'FR', 'GB', 'GR', 'GT', 'HK', 'HN', 'HU', 'ID', 'IE', 'IL', 'IN', 'IS', 'IT', 'JO', 'JP', 'KW', 'LB', 'LI', 'LT', 'LU', 'LV', 'MA', 'MC', 'MT', 'MX', 'MY', 'NI', 'NL', 'NO', 'NZ', 'OM', 'PA', 'PE', 'PH', 'PL', 'PS', 'PT', 'PY', 'QA', 'RO', 'SA', 'SE', 'SG', 'SK', 'SV', 'TH', 'TN', 'TR', 'TW', 'US', 'UY', 'VN', 'ZA'], 'disc_number': 1, 'duration_ms': 231739, 'explicit': True, 'external_ids': {'isrc': 'USUM72110013'}, 'external_urls': {'spotify': 'https://open.spotify.com/track/1IY46WkIINigH71KTv7Uv2'}, 'href': 'https://api.spotify.com/v1/tracks/1IY46WkIINigH71KTv7Uv2', 'id': '1IY46WkIINigH71KTv7Uv2', 'is_local': False, 'name': 'All I Do', 'popularity': 58, 'preview_url': 'https://p.scdn.co/mp3-preview/764c29ffcf95566aa48669649c601733b6cc4d69?cid=7c396993dafd46c3b30341981ec56217', 'track_number': 1,
'type': 'track', 'uri': 'spotify:track:1IY46WkIINigH71KTv7Uv2'}, {'album': {'album_type': 'ALBUM', 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/1McMsnEElThX1knmY4oliG'}, 'href': 'https://api.spotify.com/v1/artists/1McMsnEElThX1knmY4oliG', 'id': '1McMsnEElThX1knmY4oliG', 'name': 'Olivia Rodrigo', 'type': 'artist', 'uri': 'spotify:artist:1McMsnEElThX1knmY4oliG'}], 'available_markets': ['AD', 'AE', 'AR', 'AT', 'AU', 'BE', 'BG', 'BH', 'BO', 'BR', 'CA', 'CH', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'FI', 'FR', 'GB', 'GR', 'GT', 'HK', 'HN', 'HU', 'ID', 'IE', 'IL', 'IN', 'IS', 'IT', 'JO', 'JP', 'KW', 'LB', 'LI', 'LT', 'LU', 'LV', 'MA', 'MC', 'MT', 'MX', 'MY', 'NI', 'NL', 'NO', 'NZ', 'OM', 'PA', 'PE', 'PH', 'PL', 'PS', 'PT', 'PY', 'QA', 'RO', 'SA', 'SE', 'SG', 'SK', 'SV', 'TH', 'TN', 'TR', 'TW', 'US', 'UY', 'VN', 'ZA'], 'external_urls': {'spotify': 'https://open.spotify.com/album/6s84u2TUpR3wdUv4NgKA2j'}, 'href': 'https://api.spotify.com/v1/albums/6s84u2TUpR3wdUv4NgKA2j', 'id': '6s84u2TUpR3wdUv4NgKA2j', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b273a91c10fe9472d9bd89802e5a', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e02a91c10fe9472d9bd89802e5a', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d00004851a91c10fe9472d9bd89802e5a', 'width': 64}], 'name': 'SOUR', 'release_date': '2021-05-21', 'release_date_precision': 'day', 'total_tracks': 11, 'type': 'album', 'uri': 'spotify:album:6s84u2TUpR3wdUv4NgKA2j'}, 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/1McMsnEElThX1knmY4oliG'}, 'href': 'https://api.spotify.com/v1/artists/1McMsnEElThX1knmY4oliG', 'id': '1McMsnEElThX1knmY4oliG', 'name': 'Olivia Rodrigo', 'type': 'artist', 'uri': 'spotify:artist:1McMsnEElThX1knmY4oliG'}], 'available_markets': ['AD', 'AE', 'AR', 'AT', 'AU', 'BE', 'BG', 'BH', 'BO', 'BR', 'CA', 'CH', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'FI', 'FR', 'GB', 'GR', 'GT', 'HK', 'HN', 'HU', 'ID', 'IE', 'IL', 'IN', 'IS', 'IT', 'JO', 'JP', 'KW', 'LB', 'LI', 'LT', 'LU', 'LV', 'MA', 'MC', 'MT', 'MX', 'MY', 'NI', 'NL', 'NO', 'NZ', 'OM', 'PA', 'PE', 'PH', 'PL', 'PS', 'PT', 'PY', 'QA', 'RO', 'SA', 'SE', 'SG', 'SK', 'SV', 'TH', 'TN', 'TR', 'TW', 'US', 'UY', 'VN', 'ZA'], 'disc_number': 1, 'duration_ms': 143746, 'explicit': True, 'external_ids': {'isrc': 'USUG12101242'}, 'external_urls': {'spotify': 'https://open.spotify.com/track/6SRsiMl7w1USE4mFqrOhHC'}, 'href': 'https://api.spotify.com/v1/tracks/6SRsiMl7w1USE4mFqrOhHC', 'id': '6SRsiMl7w1USE4mFqrOhHC', 'is_local': False, 'name': 'brutal', 'popularity': 93, 'preview_url': 'https://p.scdn.co/mp3-preview/e26c087eb4410d2372aa283d2de02e31e3f7bc81?cid=7c396993dafd46c3b30341981ec56217', 'track_number': 1, 'type': 'track', 'uri': 'spotify:track:6SRsiMl7w1USE4mFqrOhHC'}, {'album': {'album_type': 'ALBUM', 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/6l3HvQ5sa6mXTsMTB19rO5'}, 'href': 'https://api.spotify.com/v1/artists/6l3HvQ5sa6mXTsMTB19rO5', 'id': '6l3HvQ5sa6mXTsMTB19rO5', 'name': 'J. Cole', 'type': 'artist', 'uri': 'spotify:artist:6l3HvQ5sa6mXTsMTB19rO5'}], 'available_markets': ['AD', 'AE', 'AR', 'AT', 'AU', 'BE', 'BG', 'BH', 'BO', 'BR', 'CA', 'CH', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'FI', 'FR', 'GB', 'GR', 'GT', 'HK', 'HN', 'HU', 'ID', 'IE', 'IL', 'IN', 'IS', 'IT', 'JO', 'JP', 'KW', 'LB', 'LI', 'LT', 'LU', 'LV', 'MA', 'MC', 'MT', 'MX', 'MY', 'NI', 'NL', 'NO', 'NZ', 'OM', 'PA', 'PE', 'PH', 'PL', 'PS', 'PT', 'PY', 'QA', 'RO', 'SA', 'SE', 'SG', 'SK', 'SV', 'TH', 'TN', 'TR', 'TW', 'US', 'UY', 'VN', 'ZA'], 'external_urls': {'spotify': 'https://open.spotify.com/album/4JAvwK4APPArjIsOdGoJXX'}, 'href': 'https://api.spotify.com/v1/albums/4JAvwK4APPArjIsOdGoJXX', 'id': '4JAvwK4APPArjIsOdGoJXX', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b27310e6745bb2f179dd3616b85f', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e0210e6745bb2f179dd3616b85f', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d0000485110e6745bb2f179dd3616b85f', 'width': 64}], 'name': 'The Off-Season', 'release_date': '2021-05-14', 'release_date_precision': 'day', 'total_tracks': 12, 'type': 'album', 'uri': 'spotify:album:4JAvwK4APPArjIsOdGoJXX'}, 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/6l3HvQ5sa6mXTsMTB19rO5'}, 'href': 'https://api.spotify.com/v1/artists/6l3HvQ5sa6mXTsMTB19rO5', 'id': '6l3HvQ5sa6mXTsMTB19rO5', 'name': 'J. Cole', 'type': 'artist', 'uri': 'spotify:artist:6l3HvQ5sa6mXTsMTB19rO5'}], 'available_markets': ['AD', 'AE', 'AR', 'AT', 'AU', 'BE', 'BG', 'BH', 'BO', 'BR', 'CA', 'CH', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'FI', 'FR', 'GB', 'GR', 'GT', 'HK', 'HN', 'HU', 'ID', 'IE', 'IL', 'IN', 'IS', 'IT', 'JO', 'JP', 'KW', 'LB', 'LI', 'LT', 'LU', 'LV', 'MA', 'MC', 'MT', 'MX', 'MY', 'NI', 'NL', 'NO', 'NZ', 'OM', 'PA', 'PE', 'PH', 'PL', 'PS', 'PT', 'PY', 'QA', 'RO', 'SA', 'SE', 'SG', 'SK', 'SV', 'TH', 'TN', 'TR', 'TW', 'US', 'UY', 'VN', 'ZA'], 'disc_number': 1, 'duration_ms': 196946, 'explicit': True, 'external_ids': {'isrc': 'QMJMT2103630'}, 'external_urls': {'spotify': 'https://open.spotify.com/track/5R691ipUYRDYW6ehapjoj6'}, 'href': 'https://api.spotify.com/v1/tracks/5R691ipUYRDYW6ehapjoj6', 'id': '5R691ipUYRDYW6ehapjoj6', 'is_local': False, 'name': '9 5 . s o u t h', 'popularity': 81, 'preview_url': 'https://p.scdn.co/mp3-preview/bbb48fc17381e55e0729fd2e1e0c5fabd2f23ea1?cid=7c396993dafd46c3b30341981ec56217', 'track_number': 1, 'type': 'track', 'uri': 'spotify:track:5R691ipUYRDYW6ehapjoj6'}, {'album': {'album_type': 'ALBUM', 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/1VPmR4DJC1PlOtd0IADAO0'}, 'href': 'https://api.spotify.com/v1/artists/1VPmR4DJC1PlOtd0IADAO0', 'id': '1VPmR4DJC1PlOtd0IADAO0', 'name': '$uicideboy$', 'type': 'artist', 'uri': 'spotify:artist:1VPmR4DJC1PlOtd0IADAO0'}], 'available_markets': ['AD', 'AE', 'AR', 'AT', 'AU', 'BE', 'BG', 'BH', 'BO', 'BR', 'CA', 'CH', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'FI', 'FR', 'GB', 'GR', 'GT', 'HK', 'HN', 'HU', 'ID', 'IE', 'IL', 'IN', 'IS', 'IT', 'JO', 'JP', 'KW', 'LB', 'LI', 'LT', 'LU', 'LV', 'MA', 'MC', 'MT', 'MX', 'MY', 'NI', 'NL', 'NO', 'NZ', 'OM', 'PA', 'PE', 'PH', 'PL', 'PS', 'PT', 'PY', 'QA', 'RO', 'SA', 'SE', 'SG', 'SK', 'SV', 'TH', 'TN', 'TR', 'TW', 'US', 'UY', 'VN', 'ZA'], 'external_urls': {'spotify': 'https://open.spotify.com/album/2ivOxIKDHxEo6WMD9m3ytn'}, 'href': 'https://api.spotify.com/v1/albums/2ivOxIKDHxEo6WMD9m3ytn', 'id': '2ivOxIKDHxEo6WMD9m3ytn', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b2739db03c8368f127291ced4263', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e029db03c8368f127291ced4263', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d000048519db03c8368f127291ced4263', 'width': 64}], 'name': 'I Want to Die In New Orleans', 'release_date': '2018-09-07', 'release_date_precision': 'day', 'total_tracks': 14, 'type': 'album', 'uri': 'spotify:album:2ivOxIKDHxEo6WMD9m3ytn'}, 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/1VPmR4DJC1PlOtd0IADAO0'}, 'href': 'https://api.spotify.com/v1/artists/1VPmR4DJC1PlOtd0IADAO0', 'id': '1VPmR4DJC1PlOtd0IADAO0', 'name': '$uicideboy$', 'type': 'artist', 'uri': 'spotify:artist:1VPmR4DJC1PlOtd0IADAO0'}], 'available_markets': ['AD', 'AE', 'AR', 'AT', 'AU', 'BE', 'BG', 'BH', 'BO', 'BR', 'CA', 'CH', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'FI', 'FR', 'GB', 'GR', 'GT', 'HK', 'HN', 'HU', 'ID', 'IE', 'IL', 'IN', 'IS', 'IT', 'JO', 'JP', 'KW', 'LB', 'LI', 'LT', 'LU', 'LV', 'MA', 'MC', 'MT', 'MX', 'MY', 'NI', 'NL', 'NO', 'NZ', 'OM', 'PA', 'PE', 'PH', 'PL', 'PS', 'PT', 'PY', 'QA', 'RO', 'SA', 'SE', 'SG', 'SK', 'SV', 'TH', 'TN', 'TR', 'TW', 'US', 'UY', 'VN', 'ZA'], 'disc_number': 1, 'duration_ms': 203897, 'explicit': True, 'external_ids': {'isrc': 'QZAPK1700041'}, 'external_urls': {'spotify': 'https://open.spotify.com/track/2XSrt1dcuOXPgl3B4bxmBz'}, 'href': 'https://api.spotify.com/v1/tracks/2XSrt1dcuOXPgl3B4bxmBz', 'id': '2XSrt1dcuOXPgl3B4bxmBz', 'is_local': False, 'name': 'Carrollton', 'popularity': 70, 'preview_url': 'https://p.scdn.co/mp3-preview/5defe8c6ca8d4b4069ec986e517c6ad87a90a9ea?cid=7c396993dafd46c3b30341981ec56217', 'track_number': 12, 'type': 'track', 'uri': 'spotify:track:2XSrt1dcuOXPgl3B4bxmBz'}]

artists = [{'external_urls': {'spotify': 'https://open.spotify.com/artist/1VPmR4DJC1PlOtd0IADAO0'}, 'followers': {'href': None, 'total': 3328481}, 'genres': ['dark trap', 'new orleans rap', 'underground hip hop'], 'href': 'https://api.spotify.com/v1/artists/1VPmR4DJC1PlOtd0IADAO0', 'id': '1VPmR4DJC1PlOtd0IADAO0', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/2d1e0c2edbb23b01d494b21a0ace0a56dfdae968', 'width': 640}, {'height': 320, 'url': 'https://i.scdn.co/image/2ab308b9a01d55be2ff34bdf0e26d8b36819f3cd', 'width': 320}, {'height': 160, 'url': 'https://i.scdn.co/image/f0eded2a810fd4e931c9e12c661a258e2fa88bad', 'width': 160}], 'name': '$uicideboy$', 'popularity': 85, 'type': 'artist', 'uri': 'spotify:artist:1VPmR4DJC1PlOtd0IADAO0'}, {'external_urls': {'spotify': 'https://open.spotify.com/artist/56ZTgzPBDge0OvCGgMO3OY'}, 'followers': {'href': None, 'total': 1195200}, 'genres': ['art pop', 'baltimore indie', 'dream pop', 'dreamo', 'indie pop', 'indie rock', 'modern dream pop'], 'href': 'https://api.spotify.com/v1/artists/56ZTgzPBDge0OvCGgMO3OY', 'id': '56ZTgzPBDge0OvCGgMO3OY', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/b34aff7ff25bb5882346fee11f05a46f38fbfbd3', 'width': 640}, {'height': 320, 'url': 'https://i.scdn.co/image/13fd407d5bd9a056e4f2cbdbbe27f2e44e0d0a4b', 'width': 320}, {'height': 160, 'url': 'https://i.scdn.co/image/ae5990c725d013e72cef504be145116707f2e2db', 'width': 160}], 'name': 'Beach House', 'popularity': 74, 'type': 'artist', 'uri': 'spotify:artist:56ZTgzPBDge0OvCGgMO3OY'}, {'external_urls': {'spotify': 'https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4'}, 'followers': {'href': None, 'total': 55389242}, 'genres': ['canadian hip hop', 'canadian pop', 'hip hop', 'pop rap', 'rap', 'toronto rap'], 'href': 'https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4', 'id': '3TVXtAsR1Inumwj472S9r4', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/60cfab40c6bb160a1906be45276829d430058005', 'width': 640}, {'height': 320, 'url': 'https://i.scdn.co/image/5ea794cf832550943d5f8122afcf5f23ee9d85b7', 'width': 320}, {'height': 160, 'url': 'https://i.scdn.co/image/8eaace74aaca82eaccde400bbcab2653b9cf86e1', 'width': 160}], 'name': 'Drake', 'popularity': 98, 'type': 'artist', 'uri': 'spotify:artist:3TVXtAsR1Inumwj472S9r4'}, {'external_urls': {'spotify': 'https://open.spotify.com/artist/5pKCCKE2ajJHZ9KAiaK11H'}, 'followers': {'href': None, 'total': 43376804}, 'genres': ['barbadian pop', 'dance pop', 'pop', 'post-teen pop', 'urban contemporary'], 'href': 'https://api.spotify.com/v1/artists/5pKCCKE2ajJHZ9KAiaK11H', 'id': '5pKCCKE2ajJHZ9KAiaK11H', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/1fc2f537d678d701d7d143a8fd4f0c2f29fbde22', 'width': 640}, {'height': 320, 'url': 'https://i.scdn.co/image/e8a018bfd60bf25519fd4dc8ca941263afa66651', 'width': 320}, {'height': 160, 'url': 'https://i.scdn.co/image/9dfb8baea10b330f5400922ec4d40d01922e805b', 'width': 160}], 'name': 'Rihanna', 'popularity': 92, 'type': 'artist', 'uri': 'spotify:artist:5pKCCKE2ajJHZ9KAiaK11H'}, {'external_urls': {'spotify': 'https://open.spotify.com/artist/0LcJLqbBmaGUft1e9Mm8HV'}, 'followers': {'href': None, 'total': 5859051}, 'genres': ['europop', 'swedish pop'], 'href': 'https://api.spotify.com/v1/artists/0LcJLqbBmaGUft1e9Mm8HV', 'id': '0LcJLqbBmaGUft1e9Mm8HV', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/6dec77bd3cdd0c634a1c9400c3c7fe8b0f1aa56e', 'width': 640}, {'height': 320, 'url': 'https://i.scdn.co/image/a595c3e9d2fc6dbd440c7734e8302bc58b3946df', 'width': 320}, {'height': 160, 'url': 'https://i.scdn.co/image/a4edd68c1eb05782afb31daf5f7b6219ce7faca0', 'width': 160}], 'name': 'ABBA', 'popularity': 82, 'type': 'artist', 'uri': 'spotify:artist:0LcJLqbBmaGUft1e9Mm8HV'}, {'external_urls': {'spotify': 'https://open.spotify.com/artist/4xRYI6VqpkE3UwrDrAZL8L'}, 'followers': {'href': None, 'total': 5388146}, 'genres': ['conscious hip hop', 'dmv rap', 'hip hop', 'pop rap', 'rap'], 'href': 'https://api.spotify.com/v1/artists/4xRYI6VqpkE3UwrDrAZL8L', 'id': '4xRYI6VqpkE3UwrDrAZL8L', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/efa0b73c2cdaf40b1767b4b1e1254b1cfc5b51db', 'width': 640}, {'height': 320, 'url': 'https://i.scdn.co/image/0caa5d73bd4ffa679036cf701507adc4d363478d', 'width': 320}, {'height': 160, 'url': 'https://i.scdn.co/image/9935c77a1d9ec285adb620a51f63e6611957879e', 'width': 160}], 'name': 'Logic', 'popularity': 83, 'type': 'artist', 'uri': 'spotify:artist:4xRYI6VqpkE3UwrDrAZL8L'}, {'external_urls': {'spotify': 'https://open.spotify.com/artist/1Xyo4u8uXC1ZmMpatF05PJ'}, 'followers': {'href': None, 'total': 33629518}, 'genres': ['canadian contemporary r&b', 'canadian pop', 'pop'], 'href': 'https://api.spotify.com/v1/artists/1Xyo4u8uXC1ZmMpatF05PJ', 'id': '1Xyo4u8uXC1ZmMpatF05PJ', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/37376dba0623c33923eae9d234e5e199b76d227f', 'width': 640}, {'height': 320, 'url': 'https://i.scdn.co/image/bf5643a4223bb6483f5b0b981bce1cf7b5f92f84', 'width': 320}, {'height': 160, 'url': 'https://i.scdn.co/image/8a188b7236f3c78416a3f75c9da52957ed3bcb9b', 'width': 160}], 'name': 'The Weeknd', 'popularity': 96, 'type': 'artist', 'uri': 'spotify:artist:1Xyo4u8uXC1ZmMpatF05PJ'}, {'external_urls': {'spotify': 'https://open.spotify.com/artist/3WrFJ7ztbogyGnTHbHJFl2'}, 'followers': {'href': None, 'total': 19781379}, 'genres': ['beatlesque', 'british invasion', 'classic rock', 'merseybeat', 'psychedelic rock', 'rock'], 'href': 'https://api.spotify.com/v1/artists/3WrFJ7ztbogyGnTHbHJFl2', 'id': '3WrFJ7ztbogyGnTHbHJFl2', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/6b2a709752ef9c7aaf0d270344157f6cd2e0f1a7', 'width': 640}, {'height': 320, 'url': 'https://i.scdn.co/image/1047bf172446f2a815a99ab0a0395099d621be51', 'width': 320}, {'height': 160, 'url': 'https://i.scdn.co/image/0561b59a91a5e904ad2d192747715688d5f05012', 'width': 160}], 'name': 'The Beatles', 'popularity': 88, 'type': 'artist', 'uri': 'spotify:artist:3WrFJ7ztbogyGnTHbHJFl2'}, {'external_urls': {'spotify': 'https://open.spotify.com/artist/5INjqkS1o8h1imAzPqGZBb'}, 'followers': {'href': None, 'total': 4980648}, 'genres': ['australian psych', 'neo-psychedelic'], 'href': 'https://api.spotify.com/v1/artists/5INjqkS1o8h1imAzPqGZBb', 'id': '5INjqkS1o8h1imAzPqGZBb', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/f8b1f2a47a920deb20fd3daf9031b2098b956e92', 'width': 640}, {'height': 320, 'url': 'https://i.scdn.co/image/da62265310c9145d17e3d1b9ee33e89ff47ec64f', 'width': 320}, {'height': 160, 'url': 'https://i.scdn.co/image/b23873775979039c1ee3103954ae302c8a618c6f', 'width': 160}], 'name': 'Tame Impala', 'popularity': 82, 'type': 'artist', 'uri': 'spotify:artist:5INjqkS1o8h1imAzPqGZBb'}, {'external_urls': {'spotify': 'https://open.spotify.com/artist/7MoIc5s9KXolCBH1fy9kkw'}, 'followers': {'href': None, 'total': 303396}, 'genres': ['art pop', 'eugene indie', 'indie pop', 'indie rock', 'philly indie'], 'href': 'https://api.spotify.com/v1/artists/7MoIc5s9KXolCBH1fy9kkw', 'id': '7MoIc5s9KXolCBH1fy9kkw', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/5f81d58a6a1de44b28148055a4fadfe46ab38bcd', 'width': 640}, {'height': 320, 'url': 'https://i.scdn.co/image/7f22a79e06054aa77e480549441115f23112a054', 'width': 320}, {'height': 160, 'url': 'https://i.scdn.co/image/3b520168e86bb7a6ed317d700aa8afc893cb7be7', 'width': 160}], 'name': 'Japanese Breakfast', 'popularity': 67, 'type': 'artist', 'uri': 'spotify:artist:7MoIc5s9KXolCBH1fy9kkw'}]

user = {'display_name': 'jackwinford', 'external_urls': {'spotify': 'https://open.spotify.com/user/jackwinford'}, 'followers': {'href': None, 'total': 17}, 'href': 'https://api.spotify.com/v1/users/jackwinford', 'id': 'jackwinford', 'images': [{'height': None, 'url': 'https://i.scdn.co/image/ab6775700000ee851b1fe4b55885c1747c550445', 'width': None}], 'type': 'user', 'uri': 'spotify:user:jackwinford'}

import os
from unittest import TestCase
import unittest
from models import db, User
from update_database import update_user

os.environ['DATABASE_URL'] = 'postgresql://statify-test'

from app import app

db.create_all()

class UpdateDatabaseTestCase(TestCase):
    """test update_database"""

    def setUp(self):
        """ensure database is empty."""
        db.drop_all()
        db.create_all()

        new_user = update_user(user, 'token')

        self.new_user = new_user
    
    def tearDown(self):
        resp = super().tearDown()
        db.session.rollback()
        return resp

    def test_update_user(self):
        """test if the update user function works"""

        new_user = update_user(user, 'token')


        self.assertEqual(new_user.id, 1)
        self.assertEqual(new_user.display_name, 'jackwinford')
        self.assertEqual(new_user.profile_pic_url, 'https://i.scdn.co/image/ab6775700000ee851b1fe4b55885c1747c550445')

if __name__ == '__main__':
    unittest.main()