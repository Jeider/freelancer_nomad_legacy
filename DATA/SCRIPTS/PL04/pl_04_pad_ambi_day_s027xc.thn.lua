duration=10000

entities={
	{
		entity_name="ambi_Layer_Pl_04_Pad_ambi_day",
		type=SCENE,
		template_name="",
		lt_grp=0,
		srt_grp=0,
		usr_flg=0,
		spatialprops={
			pos={
				0,
				0,
				0
			},
			orient={
				{
					1,
					0,
					0
				},
				{
					0,
					1,
					0
				},
				{
					0,
					0,
					1
				}
			}
		},
		up=Y_AXIS,
		front=Z_AXIS,
		ambient={
			0,
			0,
			0
		}
	},
	{
		entity_name="ambi_LtG23_Sky_Amb",
		type=LIGHT,
		template_name="",
		lt_grp=23,
		srt_grp=0,
		usr_flg=0,
		spatialprops={
			pos={
				82.500336,
				-7.632787,
				-14.768388
			},
			orient={
				{
					1,
					0,
					0
				},
				{
					0,
					1,
					0
				},
				{
					0,
					0,
					1
				}
			}
		},
		lightprops={
			on=Y,
			color={
				255,
				255,
				255
			},
			diffuse={
				0,
				0,
				0
			},
			specular={
				0,
				0,
				0
			},
			ambient={
				0.12549,
				0.043137,
				0.07451000000000001
			},
			direction={
				0,
				0,
				1
			},
			range=2000,
			cutoff=98.999977,
			type=L_DIRECT,
			theta=90,
			atten={
				1,
				0,
				0
			}
		}
	},
	{
		entity_name="ambi_LtG09_Planet_Sky",
		type=LIGHT,
		template_name="",
		lt_grp=9,
		srt_grp=0,
		usr_flg=0,
		spatialprops={
			pos={
				85.060242,
				-7.632787,
				-13.618918
			},
			orient={
				{
					-0.867564,
					0,
					-0.497326
				},
				{
					0.18884,
					0.925106,
					-0.329422
				},
				{
					0.460079,
					-0.379709,
					-0.802588
				}
			}
		},
		lightprops={
			on=Y,
			color={
				255,
				255,
				255
			},
			diffuse={
				1,
				0.584314,
				0.164706
			},
			specular={
				0,
				0,
				0
			},
			ambient={
				0.27451,
				0.223529,
				0.27451
			},
			direction={
				0,
				0,
				1
			},
			range=2000,
			cutoff=98.999977,
			type=L_DIRECT,
			theta=90,
			atten={
				1,
				0,
				0
			}
		}
	},
	{
		entity_name="ambi_LtG09_Tunnel_Point",
		type=LIGHT,
		template_name="",
		lt_grp=9,
		srt_grp=0,
		usr_flg=0,
		spatialprops={
			pos={
				-127.909325,
				10.271246,
				-77.275757
			},
			orient={
				{
					1,
					0,
					0
				},
				{
					0,
					1,
					0
				},
				{
					0,
					0,
					1
				}
			}
		},
		lightprops={
			on=Y,
			color={
				255,
				255,
				255
			},
			diffuse={
				0.952941,
				0.952941,
				0.521569
			},
			specular={
				0,
				0,
				0
			},
			ambient={
				0,
				0,
				0
			},
			direction={
				0,
				0,
				1
			},
			range=70,
			cutoff=98.999977,
			type=L_POINT,
			theta=90,
			atten={
				1,
				0,
				0
			}
		}
	},
	{
		entity_name="ambi_skydome_clouds_wavy",
		type=COMPOUND,
		template_name="skydome_clouds_wavy",
		lt_grp=22,
		srt_grp=-99,
		usr_flg=2,
		flags=LIT_DYNAMIC,
		spatialprops={
			pos={
				82.500336,
				-7.632787,
				-14.768388
			},
			orient={
				{
					-0.078681,
					0,
					0.9969
				},
				{
					0,
					1,
					0
				},
				{
					-0.9969,
					0,
					-0.078681
				}
			}
		},
		userprops={
			category="Prop",
			NoFog="y"
		}
	},
	{
		entity_name="ambi_skydome_sky_blank",
		type=COMPOUND,
		template_name="skydome_sky_blank",
		lt_grp=23,
		srt_grp=-100,
		usr_flg=2,
		flags=LIT_DYNAMIC,
		spatialprops={
			pos={
				0,
				0,
				0
			},
			orient={
				{
					1,
					0,
					0
				},
				{
					0,
					1,
					0
				},
				{
					0,
					0,
					1
				}
			}
		},
		userprops={
			category="Prop",
			NoFog="y"
		}
	},
	{
		entity_name="ambi_LtG22_Clouds_Amb",
		type=LIGHT,
		template_name="",
		lt_grp=22,
		srt_grp=0,
		usr_flg=0,
		spatialprops={
			pos={
				82.500336,
				-7.632787,
				-14.768388
			},
			orient={
				{
					1,
					0,
					0
				},
				{
					0,
					1,
					0
				},
				{
					0,
					0,
					1
				}
			}
		},
		lightprops={
			on=Y,
			color={
				255,
				255,
				255
			},
			diffuse={
				0,
				0,
				0
			},
			specular={
				0,
				0,
				0
			},
			ambient={
				0.937255,
				0.560784,
				0.337255
			},
			direction={
				0,
				0,
				1
			},
			range=2000,
			cutoff=98.999977,
			type=L_DIRECT,
			theta=90,
			atten={
				1,
				0,
				0
			}
		}
	},
	{
		entity_name="ambi_LtG23_Sky_HorizonGlow",
		type=LIGHT,
		template_name="",
		lt_grp=23,
		srt_grp=0,
		usr_flg=0,
		spatialprops={
			pos={
				0,
				637.920837,
				0
			},
			orient={
				{
					1,
					0,
					0
				},
				{
					0,
					1,
					0
				},
				{
					0,
					0,
					1
				}
			}
		},
		lightprops={
			on=Y,
			color={
				255,
				255,
				255
			},
			diffuse={
				0.886275,
				0.203922,
				0.290196
			},
			specular={
				0,
				0,
				0
			},
			ambient={
				0,
				0,
				0
			},
			direction={
				0,
				-1,
				0
			},
			range=1000000,
			cutoff=180,
			type=L_SPOT,
			theta=169.999954,
			atten={
				1,
				0,
				0
			}
		}
	},
	{
		entity_name="ambi_LtG09_Tunnel_Point02",
		type=LIGHT,
		template_name="",
		lt_grp=9,
		srt_grp=0,
		usr_flg=0,
		spatialprops={
			pos={
				-127.909325,
				10.271246,
				-77.275757
			},
			orient={
				{
					1,
					0,
					0
				},
				{
					0,
					1,
					0
				},
				{
					0,
					0,
					1
				}
			}
		},
		lightprops={
			on=Y,
			color={
				255,
				255,
				255
			},
			diffuse={
				0.952941,
				0.952941,
				0.521569
			},
			specular={
				0,
				0,
				0
			},
			ambient={
				0,
				0,
				0
			},
			direction={
				0,
				0,
				1
			},
			range=80,
			cutoff=98.999977,
			type=L_POINT,
			theta=90,
			atten={
				1,
				0,
				0
			}
		}
	}
}

events={
	{
		0,
		START_SPATIAL_PROP_ANIM,
		{
			"ambi_skydome_clouds_wavy"
		},
		{
			duration=10000,
			target_type=ROOT,
			spatialprops={
				axisrot={
					360,
					Y_AXIS
				}
			},
			param_curve={
				CLSID="FreeFormPCurve",
				points={
					{
						0,
						0,
						0,
						0.952381
					},
					{
						1,
						1,
						0.8823530000000001,
						0
					}
				}
			},
			pcurve_period=7143534
		}
	},
	{
		0,
		START_FOG_PROP_ANIM,
		{
			"ambi_Layer_Pl_04_Pad_ambi_day"
		},
		{
			duration=0,
			fogprops={
				fogon=Y,
				fogcolor={
					32,
					30,
					32
				},
				fogmode=F_LINEAR,
				fogstart=-100,
				fogend=2500
			}
		}
	},
	{
		30.504,
		START_LIGHT_PROP_ANIM,
		{
			"ambi_LtG09_Tunnel_Point02"
		},
		{
			duration=0,
			lightprops={
				on=N
			}
		}
	}
}

